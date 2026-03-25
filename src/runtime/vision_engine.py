import cv2
import mediapipe as mp
import numpy as np
import pickle
from pathlib import Path
import sys

# Add project root to path for imports
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.features.extractor import HandFeatureExtractor

class PianoStateMachine:
    """
    Converts binary (Hover/Press) predictions into 4-state logic.
    0: Hover, 1: Press, 2: Hold, 3: Release
    """
    HOVER = 0
    PRESS = 1
    HOLD = 2
    RELEASE = 3

    def __init__(self):
        self.prev_state_binary = 0 # 0=Hover, 1=Press

    def update(self, predicted_binary):
        # predicted_binary: 0 (Hover) or 1 (Press) from Model
        curr = predicted_binary
        prev = self.prev_state_binary

        result = self.HOVER

        if prev == 0 and curr == 1:
            result = self.PRESS
        elif prev == 1 and curr == 1:
            result = self.HOLD
        elif prev == 1 and curr == 0:
            result = self.RELEASE
        elif prev == 0 and curr == 0:
            result = self.HOVER

        self.prev_state_binary = curr
        return result

class VisionEngine:
    def __init__(self, model_path="models/rf_model.pkl"):
        self.extractor = HandFeatureExtractor()
        self.fsm = PianoStateMachine()
        self.model = self._load_model(model_path)

        # MediaPipe Setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7
        )
        self.cap = cv2.VideoCapture(0)

    def _load_model(self, path):
        p = Path(path)
        if not p.exists():
            print(f"Warning: Model not found at {p}. Predictions will be dummy.")
            return None
        with open(p, 'rb') as f:
            return pickle.load(f)

    def run(self):
        print("Starting PianoMotion Vision Engine...")
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret: break

            # Preprocessing
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            state_idx = 0
            state_name = "HOVER"

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # 1. Extract Features (Strict Parity)
                    # Assuming fixed distance_cm or dynamic if you have ArUco logic here
                    features = self.extractor.process_live(hand_landmarks.landmark)

                    # 2. Inference
                    pred_binary = 0
                    if self.model and features is not None:
                        try:
                            # XGBoost expects DMatrix or array; sklearn wrapper expects array
                            pred_binary = int(self.model.predict(features)[0])
                            # Check if model outputs 0/1 or other labels
                            # Assuming 0=Hover, 1=Press for binary classifier
                        except Exception as e:
                            print(f"Inference Error: {e}")

                    # 3. State Machine
                    state_idx = self.fsm.update(pred_binary)
                    state_names = ["HOVER", "PRESS", "HOLD", "RELEASE"]
                    state_name = state_names[state_idx]

                    # Visualization
                    mp.solutions.drawing_utils.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # Overlay
            color = (0, 255, 0) if state_idx in [1, 2] else (0, 0, 255)
            cv2.putText(frame, f"State: {state_name}", (50, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
            cv2.putText(frame, f"State: {state_name}", (50, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            # Keyboard Hints
            h, w = frame.shape[:2]
            cv2.putText(frame, "[ESC] Quit", (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)
            cv2.putText(frame, "[ESC] Quit", (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cv2.imshow('PianoMotion Live', frame)
            if cv2.waitKey(5) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    VisionEngine().run()
