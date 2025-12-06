import cv2
import numpy as np
import threading
import time
import json
import os
import sys
import logging
from pathlib import Path
import joblib
import pygame

# Ensure src is importable
sys.path.append(str(Path(__file__).resolve().parent))

try:
    from cv2 import aruco
except ImportError:
    import cv2.aruco as aruco

import mediapipe as mp

# Import Centralized Modules
from src.features.extractor import HandFeatureExtractor
from src.runtime.vision_engine import PianoStateMachine

# --- CONFIGURATION (Merged) ---
CONFIG = {
    'CAM_ID': 0,
    'WIDTH': 1280,
    'HEIGHT': 720,
    # Digital Twin Config (Pixel Units)
    'MARKER_SIZE': 200.0,    # 3D Unit = 1 Pixel (Arbitrary scale for Viz)
    'SAFETY_GAP': 50.0,
    'BORDER_WIDTH': 20.0,
    'KEY_WIDTH': 100.0,
    'KEY_HEIGHT': 400.0,
    'NUM_KEYS': 7,
    # ML Config
    'MODEL_PATH': Path("models/rf_model.pkl"),
    'DISTANCE_CM_DEFAULT': 115.0
}

CALIBRATION_FILE = "calibration.json"

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [PianoMotion] - %(message)s')
logger = logging.getLogger(__name__)

# --- AUDIO ENGINE ---
class SoundEngine:
    """
    Low-latency audio engine using Pygame.
    Supports Piano-like Hold/Sustain logic.
    """
    def __init__(self):
        self.sounds = {}
        self.channels = {} # key_idx -> Channel
        self.active = False
        try:
            # Try to init audio: 44.1kHz, 16-bit, stereo, small buffer
            pygame.mixer.pre_init(44100, -16, 2, 512)
            pygame.init()
            pygame.mixer.set_num_channels(32)
            self.active = True
            self._load_sounds()
        except Exception as e:
            logger.warning(f"Audio Engine Disabled: {e}")
            self.active = False

    def _load_sounds(self):
        # C Major Scale frequencies
        notes = {
            0: ('C', 261.63),
            1: ('D', 293.66),
            2: ('E', 329.63),
            3: ('F', 349.23),
            4: ('G', 392.00),
            5: ('A', 440.00),
            6: ('B', 493.88)
        }

        for idx, (name, freq) in notes.items():
            filename = f"{name}.wav"
            if Path(filename).exists():
                try:
                    self.sounds[idx] = pygame.mixer.Sound(filename)
                except:
                    self.sounds[idx] = self._generate_sine_wave(freq)
            else:
                self.sounds[idx] = self._generate_sine_wave(freq)

        logger.info("Audio Engine Ready")

    def _generate_sine_wave(self, frequency, duration=2.0):
        """
        Generates a longer sine wave for 'Hold' capability.
        Fade out handled by Channel logic.
        """
        if not self.active: return None
        try:
            sample_rate = 44100
            n_samples = int(sample_rate * duration)
            t = np.linspace(0, duration, n_samples, False)
            wave = np.sin(2 * np.pi * frequency * t) * 0.3
            audio_data = (wave * 32767).astype(np.int16)
            stereo_data = np.column_stack((audio_data, audio_data))
            return pygame.mixer.Sound(buffer=stereo_data)
        except:
            return None

    def note_on(self, key_index):
        """Starts playing a note. Replaces existing if same key."""
        if not self.active or key_index not in self.sounds: return

        try:
            # If already playing this key, stop it to restart (or let it ring if piano style?)
            # For synth hold, we want to restart or ensure it's playing loop
            if key_index in self.channels:
                 self.channels[key_index].fadeout(50) # Quick fade old

            # Find a channel
            channel = pygame.mixer.find_channel()
            if channel:
                # Play loops=-1 for infinite hold if synth, or 0 for wav
                # Assuming synthetic sine needs looping for long hold,
                # but wav piano sample decays naturally.
                # Let's assume we want to hold "as long as pressed".
                # If it's a sine wave (generated), it has duration 2.0s. loops=-1 makes it infinite.
                channel.play(self.sounds[key_index], loops=-1)
                self.channels[key_index] = channel
        except Exception as e:
            pass

    def note_off(self, key_index):
        """Stops/Fades out a note."""
        if not self.active: return

        if key_index in self.channels:
            try:
                # Piano-like release: fade out over ~300ms
                self.channels[key_index].fadeout(300)
                del self.channels[key_index]
            except:
                pass

# --- THREADED CAMERA (from VisionEngine.py) ---
class ThreadedCamera:
    """ Producer-Consumer Threaded Video Capture """
    def __init__(self, src=0):
        self.src = src
        self.capture = cv2.VideoCapture(src)
        # Force Resolution
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, CONFIG['WIDTH'])
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, CONFIG['HEIGHT'])
        self.capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

        self.lock = threading.Lock()
        self._frame = None
        self.running = True

        success, frame = self.capture.read()
        if success: self._frame = frame

        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()

    def _update(self):
        while self.running:
            if self.capture.isOpened():
                ret, frame = self.capture.read()
                if ret:
                    with self.lock:
                        self._frame = frame
                else:
                    time.sleep(0.01)
            else:
                time.sleep(0.1)

    def read(self):
        with self.lock:
            return self._frame.copy() if self._frame is not None else None

    def stop(self):
        self.running = False
        try:
            self.thread.join(timeout=1.0)
        except:
            pass
        if self.capture.isOpened():
            self.capture.release()

    def switch_camera(self):
        """Attempts to switch to the next available camera index."""
        self.stop()
        new_src = self.src + 1
        # Try finding next camera
        temp_cap = cv2.VideoCapture(new_src)
        if not temp_cap.isOpened():
            # If failed, wrap around to 0
            new_src = 0
            temp_cap.release()
            temp_cap = cv2.VideoCapture(new_src)

        temp_cap.release()

        # Re-init with new source
        logger.info(f"Switching Camera to ID: {new_src}")
        self.__init__(new_src)

# --- POSE FILTER ---
class PoseFilter:
    """
    Exponential Moving Average filter for 6DoF Pose (rvec, tvec).
    Reduces jitter when the marker is at a steep angle.
    """
    def __init__(self, alpha=0.3):
        self.alpha = alpha
        self.rvec = None
        self.tvec = None

    def update(self, rvec, tvec):
        if self.rvec is None:
            self.rvec = rvec
            self.tvec = tvec
        else:
            # Simple linear interpolation for rvec (assuming small frame-to-frame changes)
            self.rvec = self.alpha * rvec + (1 - self.alpha) * self.rvec
            self.tvec = self.alpha * tvec + (1 - self.alpha) * self.tvec
        return self.rvec, self.tvec

    def reset(self):
        self.rvec = None
        self.tvec = None

# --- CALIBRATION WIZARD (from VisionEngine.py) ---
class CalibrationWizard:
    """
    Manages the user flow for establishing a depth baseline.
    States: NEUTRAL -> ACTIVE -> SAVED
    """
    STATE_NEUTRAL = 0
    STATE_ACTIVE = 1
    STATE_SAVED = 2

    def __init__(self, filepath=CALIBRATION_FILE):
        self.filepath = filepath
        self.state = self.STATE_NEUTRAL
        self.active = False
        self.neutral_depths = []
        self.active_depths = []
        self.avg_neutral = 0.0
        self.avg_active = 0.0

        self.threshold_z = 0.02 # Default

        if os.path.exists(self.filepath):
            self.load()
            self.active = False
        else:
            self.active = True

    def start(self):
        self.active = True
        self.state = self.STATE_NEUTRAL
        self.neutral_depths = []
        self.active_depths = []
        print("Calibration Wizard Started.")

    def update(self, current_depth):
        """
        Updates the calibration process with a new depth sample.
        current_depth: 'rel_depth' (Tip Z - Wrist Z)
        Returns: Status string to display.
        """
        if not self.active: return ""

        if self.state == self.STATE_NEUTRAL:
            self.neutral_depths.append(current_depth)
            msg = "CALIBRATION: Place hand FLAT on surface. (Press SPACE to Capture)"

        elif self.state == self.STATE_ACTIVE:
            self.active_depths.append(current_depth)
            msg = "CALIBRATION: Lift hand to HOVER height. (Press SPACE to Capture)"

        elif self.state == self.STATE_SAVED:
            msg = f"CALIBRATION SAVED. Threshold: {self.threshold_z:.4f}"

        return msg

    def next_step(self):
        if self.state == self.STATE_NEUTRAL:
            if len(self.neutral_depths) > 10:
                self.avg_neutral = np.mean(self.neutral_depths)
                self.state = self.STATE_ACTIVE
                print(f"Neutral Baseline: {self.avg_neutral:.4f}")
            else:
                print("Not enough samples for Neutral.")

        elif self.state == self.STATE_ACTIVE:
            if len(self.active_depths) > 10:
                self.avg_active = np.mean(self.active_depths)

                # Calculate Threshold (Midpoint)
                self.threshold_z = (self.avg_neutral + self.avg_active) / 2.0

                self.state = self.STATE_SAVED
                self.save()
                self.active = False
                print(f"Active Baseline: {self.avg_active:.4f}")
                print(f"Threshold Set: {self.threshold_z:.4f}")
            else:
                print("Not enough samples for Active.")

    def save(self):
        data = {'threshold_z': self.threshold_z}
        with open(self.filepath, 'w') as f:
            json.dump(data, f)

    def load(self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                self.threshold_z = data.get('threshold_z', 0.02)
                print(f"Loaded Calibration: {self.threshold_z:.4f}")
        except:
            print("Failed to load calibration.")

# --- MAIN INTEGRATION ---
class PianoMotionApp:
    def __init__(self):
        self.cam = ThreadedCamera(CONFIG['CAM_ID'])
        self.audio = SoundEngine()
        self.calibration = CalibrationWizard()
        self.extractor = HandFeatureExtractor(ref_width=CONFIG['WIDTH'], ref_height=CONFIG['HEIGHT'])
        self.fsm = PianoStateMachine()

        # ML Model
        self.model = None
        self._load_model()

        # ArUco
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        self.params = aruco.DetectorParameters()
        self.detector = aruco.ArucoDetector(self.aruco_dict, self.params)

        # MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Digital Twin Points
        self.marker_points = self._generate_marker_points()
        self.piano_points, self.key_lines = self._generate_piano_points()
        self.pose_filter = PoseFilter(alpha=0.4)

        # State
        self.last_state = 0 # Hover
        self.active_key_idx = -1 # Currently pressed key
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0.0

    def _load_model(self):
        if CONFIG['MODEL_PATH'].exists():
            try:
                self.model = joblib.load(CONFIG['MODEL_PATH'])
                logger.info(f"Loaded ML Model: {CONFIG['MODEL_PATH']}")
            except Exception as e:
                logger.error(f"Failed to load ML Model: {e}")
        else:
            logger.warning("ML Model not found. Predictions will rely on Gate/Fallback.")

    def _generate_marker_points(self):
        s = CONFIG['MARKER_SIZE']
        return np.array([
            [0, 0, 0],    # Top-Left
            [s, 0, 0],    # Top-Right
            [s, s, 0],    # Bot-Right
            [0, s, 0]     # Bot-Left
        ], dtype=np.float32)

    def _generate_piano_points(self):
        start_x = CONFIG['MARKER_SIZE'] + CONFIG['SAFETY_GAP'] + CONFIG['BORDER_WIDTH']
        total_width = CONFIG['KEY_WIDTH'] * CONFIG['NUM_KEYS']
        end_x = start_x + total_width
        y_top = 0.0
        y_bot = CONFIG['KEY_HEIGHT']

        outline = np.array([
            [start_x, y_top, 0], [end_x, y_top, 0],
            [end_x, y_bot, 0], [start_x, y_bot, 0]
        ], dtype=np.float32)

        lines = []
        for i in range(1, CONFIG['NUM_KEYS']):
            x = start_x + (i * CONFIG['KEY_WIDTH'])
            lines.append([x, y_top, 0])
            lines.append([x, y_bot, 0])

        return outline, np.array(lines, dtype=np.float32)

    def estimate_intrinsics(self, w, h):
        f = w # Approx focal length
        return np.array([[f, 0, w/2], [0, f, h/2], [0, 0, 1]], dtype=np.float32)

    def get_hand_aruco_x(self, tip_norm, rvec, tvec, cam_mat, dist):
        """
        Projects Normalized Tip to ArUco Plane Z=0 to get X coordinate.
        """
        if rvec is None or tvec is None: return None

        # Ray casting
        u = tip_norm.x * CONFIG['WIDTH']
        v = tip_norm.y * CONFIG['HEIGHT']

        fx, fy = cam_mat[0,0], cam_mat[1,1]
        cx, cy = cam_mat[0,2], cam_mat[1,2]

        x_ray = (u - cx) / fx
        y_ray = (v - cy) / fy
        ray_cam = np.array([x_ray, y_ray, 1.0])

        # Plane intersection: Z=0 in marker frame
        R, _ = cv2.Rodrigues(rvec)
        # P_cam = R * P_aruco + t
        # P_cam = lambda * ray_cam
        # P_aruco.z = 0 => P_aruco = [x_a, y_a, 0]
        # lambda * ray = x_a * r1 + y_a * r2 + t

        r1 = R[:, 0]
        r2 = R[:, 1]

        A = np.column_stack((r1, r2, -ray_cam))
        b = -tvec.flatten()

        try:
            sol = np.linalg.solve(A, b)
            return sol[0] # x_a
        except:
            return None

    def _draw_ui(self, frame, state_idx, current_rel_depth, plane_found):
        h, w = frame.shape[:2]

        # 1. Background Panel for Text (Left Side or Half Screen as requested)
        # Using a semi-transparent overlay on the left 30% of screen for readability
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (int(w*0.35), h), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

        # 2. Text Configuration
        font = cv2.FONT_HERSHEY_SIMPLEX
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (0, 0, 255)
        yellow = (0, 255, 255)

        y_cursor = 50
        line_height = 40

        # 3. FPS & Status
        cv2.putText(frame, f"FPS: {self.fps:.1f}", (20, y_cursor), font, 1.0, green, 2)
        y_cursor += line_height * 1.5

        # 4. State Display
        state_str = ["HOVER", "PRESS", "HOLD", "RELEASE"][state_idx]
        state_color = green if state_idx in [1, 2] else red
        cv2.putText(frame, f"STATE: {state_str}", (20, y_cursor), font, 1.2, state_color, 3)
        y_cursor += line_height

        # 5. Technical Data
        cv2.putText(frame, f"Rel Depth: {current_rel_depth:.4f}", (20, y_cursor), font, 0.6, white, 1)
        y_cursor += line_height
        cv2.putText(frame, f"Threshold: {self.calibration.threshold_z:.4f}", (20, y_cursor), font, 0.6, white, 1)
        y_cursor += line_height

        plane_status = "DETECTED" if plane_found else "SEARCHING..."
        plane_color = green if plane_found else yellow
        cv2.putText(frame, f"ArUco Plane: {plane_status}", (20, y_cursor), font, 0.6, plane_color, 1)
        y_cursor += line_height * 2

        # 6. Instructions
        cv2.putText(frame, "--- INSTRUCTIONS ---", (20, y_cursor), font, 0.7, yellow, 2)
        y_cursor += line_height

        instructions = [
            " [C]     Start Calibration",
            " [SPACE] Next Step (Calib)",
            " [V]     Change Camera",
            " [Q]     Quit Program"
        ]

        for line in instructions:
            cv2.putText(frame, line, (20, y_cursor), font, 0.6, white, 1)
            y_cursor += line_height

    def run(self):
        print("Starting PianoMotion (Integrated)...")

        try:
            while True:
                frame = self.cam.read()
                if frame is None:
                    time.sleep(0.01)
                    continue

                # FPS Calculation
                self.frame_count += 1
                elapsed = time.time() - self.start_time
                if elapsed > 1.0:
                    self.fps = self.frame_count / elapsed
                    self.frame_count = 0
                    self.start_time = time.time()

                h, w = frame.shape[:2]
                cam_mat = self.estimate_intrinsics(w, h)
                dist = np.zeros((4,1))

                # 1. ArUco Detection & Digital Twin Visualization
                corners, ids, _ = self.detector.detectMarkers(frame)
                rvec, tvec = None, None
                plane_found = False

                if ids is not None:
                    ids_flat = ids.flatten()
                    if 0 in ids_flat:
                        idx = np.where(ids_flat == 0)[0][0]
                        c0 = corners[idx].reshape((4, 2))

                        # Use IPPE_SQUARE for better planar accuracy if available
                        flags = cv2.SOLVEPNP_IPPE_SQUARE if hasattr(cv2, 'SOLVEPNP_IPPE_SQUARE') else cv2.SOLVEPNP_ITERATIVE

                        success, rvec_raw, tvec_raw = cv2.solvePnP(self.marker_points, c0, cam_mat, dist, flags=flags)

                        if success:
                            plane_found = True
                            # Smooth Pose
                            rvec, tvec = self.pose_filter.update(rvec_raw, tvec_raw)

                            # Draw Axes
                            cv2.drawFrameAxes(frame, cam_mat, dist, rvec, tvec, 100.0)

                            # Draw Piano Grid
                            outline_2d, _ = cv2.projectPoints(self.piano_points, rvec, tvec, cam_mat, dist)
                            outline_2d = np.int32(outline_2d).reshape(-1, 2)
                            cv2.polylines(frame, [outline_2d], True, (0, 255, 255), 2)

                            lines_2d, _ = cv2.projectPoints(self.key_lines, rvec, tvec, cam_mat, dist)
                            lines_2d = np.int32(lines_2d).reshape(-1, 2)
                            for i in range(0, len(lines_2d), 2):
                                cv2.line(frame, tuple(lines_2d[i]), tuple(lines_2d[i+1]), (0, 255, 255), 1)
                    else:
                        self.pose_filter.reset()
                else:
                    self.pose_filter.reset()

                # 2. Hand Processing
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(frame_rgb)

                current_rel_depth = 0.0
                state_idx = 0 # Default Hover

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                        # A. Calculate Rel Depth (Tip Z - Wrist Z) for Calibration/Gate
                        current_rel_depth = hand_landmarks.landmark[8].z - hand_landmarks.landmark[0].z

                        # B. Feature Extraction
                        # Use dynamic distance from ArUco if available, else default
                        dynamic_dist = CONFIG['DISTANCE_CM_DEFAULT']
                        if plane_found and tvec is not None:
                            # tvec[2] is Z in meters. Convert to cm.
                            dynamic_dist = float(tvec[2][0]) * 100.0

                        features = self.extractor.process_live(
                            hand_landmarks.landmark,
                            distance_cm=dynamic_dist
                        )

                        # C. Hybrid Logic
                        if self.calibration.active:
                            pass # Pass-through
                        else:
                            is_hover_physically = False
                            if self.calibration.avg_active != 0 and self.calibration.avg_neutral != 0:
                                if self.calibration.avg_active > self.calibration.avg_neutral:
                                    if current_rel_depth > self.calibration.threshold_z: is_hover_physically = True
                                else:
                                    if current_rel_depth < self.calibration.threshold_z: is_hover_physically = True

                            if is_hover_physically:
                                state_idx = 0 # Force Hover
                            else:
                                # Run ML
                                if self.model and features is not None:
                                    try:
                                        # Ensure features are (1, N) for sklearn
                                        if len(features.shape) == 1:
                                            features = features.reshape(1, -1)

                                        pred_binary = int(self.model.predict(features)[0])
                                        state_idx = self.fsm.update(pred_binary)
                                    except Exception as e:
                                        # logger.error(f"Inference Error: {e}")
                                        pass
                                else:
                                    state_idx = 1
                                    state_idx = self.fsm.update(1)

                # 3. Audio & Key Logic
                if plane_found and results.multi_hand_landmarks:
                    lm = results.multi_hand_landmarks[0].landmark[8] # Tip
                    x_aruco = self.get_hand_aruco_x(lm, rvec, tvec, cam_mat, dist)

                    if x_aruco is not None:
                        grid_start = CONFIG['MARKER_SIZE'] + CONFIG['SAFETY_GAP'] + CONFIG['BORDER_WIDTH']
                        offset = x_aruco - grid_start
                        if offset >= 0:
                            key_idx = int(offset / CONFIG['KEY_WIDTH'])

                            if 0 <= key_idx < CONFIG['NUM_KEYS']:
                                k_center_x = grid_start + (key_idx + 0.5) * CONFIG['KEY_WIDTH']
                                k_center_y = CONFIG['KEY_HEIGHT'] / 2
                                k_pt_3d = np.array([[[k_center_x, k_center_y, 0]]], dtype=np.float32)
                                k_pt_2d, _ = cv2.projectPoints(k_pt_3d, rvec, tvec, cam_mat, dist)
                                center_px = tuple(np.int32(k_pt_2d.reshape(2)))

                                if state_idx in [1, 2]: # Press/Hold
                                    cv2.circle(frame, center_px, 10, (0, 255, 0), -1)
                                else:
                                    cv2.circle(frame, center_px, 5, (0, 255, 255), -1)

                                # Trigger Audio Logic (Sustain/Hold)
                                # State: 1 (Press), 2 (Hold) -> Note ON
                                # State: 0 (Hover), 3 (Release) -> Note OFF

                                if state_idx in [1, 2]:
                                    # If Key Changed while holding/pressing
                                    if key_idx != self.active_key_idx:
                                        if self.active_key_idx != -1:
                                            self.audio.note_off(self.active_key_idx)
                                        self.audio.note_on(key_idx)
                                        self.active_key_idx = key_idx
                                        # Visual Flash
                                        cv2.circle(frame, center_px, 20, (255, 255, 255), -1)
                                    else:
                                        # Same key, ensure visual feedback
                                        pass
                                else:
                                    # Released
                                    if self.active_key_idx != -1:
                                        self.audio.note_off(self.active_key_idx)
                                        self.active_key_idx = -1

                # If plane/hand lost but key was active, release it
                if (not plane_found or not results.multi_hand_landmarks) and self.active_key_idx != -1:
                    self.audio.note_off(self.active_key_idx)
                    self.active_key_idx = -1

                # 4. Calibration Wizard UI
                if self.calibration.active:
                    status_msg = self.calibration.update(current_rel_depth)
                    cv2.rectangle(frame, (0, h-60), (w, h), (0, 0, 0), -1)
                    cv2.putText(frame, status_msg, (20, h-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    cv2.putText(frame, f"Rel Depth: {current_rel_depth:.4f}", (10, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                else:
                    # Use the new UI helper
                    self._draw_ui(frame, state_idx, current_rel_depth, plane_found)

                self.last_state = state_idx
                cv2.imshow("PianoMotion", frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'): break
                if key == ord('c'): self.calibration.start()
                if key == ord(' '): self.calibration.next_step()
                if key == ord('v'): self.cam.switch_camera()

        finally:
            self.cam.stop()
            cv2.destroyAllWindows()
            pygame.quit()

if __name__ == "__main__":
    PianoMotionApp().run()
