import numpy as np
from collections import deque

class QueuedList:
    """Helper to mimic the rolling buffer logic from legacy code."""
    def __init__(self, maxlen=10):
        self.data = deque(maxlen=maxlen)

    def append(self, item):
        self.data.append(item)

    def get_mean(self):
        if not self.data: return 0.0
        return sum(self.data) / len(self.data)

class HandFeatureExtractor:
    """
    Centralized Source of Truth for Feature Engineering.
    Strictly implements the legacy 'append_dataset' logic for parity.
    """
    def __init__(self, buffer_size=10, ref_width=1280, ref_height=720):
        self.ref_width = ref_width
        self.ref_height = ref_height
        self.buffer_size = buffer_size

        # Legacy State Logic
        self.old_coor = None
        self.ql_disp = QueuedList(maxlen=buffer_size)
        self.ql_size = QueuedList(maxlen=buffer_size)
        self.elapsed_frames = 0

    def _to_pixel(self, landmark):
        """Converts normalized MediaPipe landmark to pixel coordinates."""
        return np.array([
            int(landmark.x * self.ref_width),
            int(landmark.y * self.ref_height)
        ])

    def _get_euclidean(self, p1, p2):
        """Matches legacy: int(p1[0]-p2[0])**2 + int(p1[1]-p2[1])**2 ..."""
        x = int(p1[0] - p2[0]) ** 2
        y = int(p1[1] - p2[1]) ** 2
        return np.sqrt(x + y)

    def process_live(self, landmarks, distance_cm=115.0):
        """
        Process a live MediaPipe landmark list.
        Returns: feature vector array.
        """
        if not landmarks:
            return None

        # 1. Convert landmarks
        try:
            wrist = self._to_pixel(landmarks[0])
            tip = self._to_pixel(landmarks[8])
            dip = self._to_pixel(landmarks[7])
            pip = self._to_pixel(landmarks[6])
            mcp = self._to_pixel(landmarks[5])
        except (IndexError, AttributeError):
            return None

        new_coor = tip # Index Tip is the reference coordinate

        # 2. Calculate Distances (Legacy Loop)
        indices_coords = [dip, pip, mcp, wrist]
        keys = ['tip2dip', 'tip2pip', 'tip2mcp', 'tip2wrist']
        feats = {}

        total_size_acc = 0.0
        for i, coord in enumerate(indices_coords):
            dist = self._get_euclidean(new_coor, coord)
            feats[keys[i]] = dist
            total_size_acc += dist

        # 3. Calculate Disp & Velocity Logic
        disp = 0.0
        accuracy = 0.0 # This is 'acceleration_disp' in legacy naming

        if self.elapsed_frames < 1 or self.old_coor is None:
            self.ql_disp.append(0)
        else:
            disp = self._get_euclidean(self.old_coor, new_coor)
            previous_velocity = self.ql_disp.get_mean()
            self.ql_disp.append(disp)
            new_velocity = self.ql_disp.get_mean()
            # accuracy = previous_velocity - new_velocity
            # (Matches legacy code exactly, though physically this is deceleration)
            accuracy = previous_velocity - new_velocity

        # 4. Calculate Size Metric
        # ql_size appends the AVERAGE of the 4 distances (sum / 4)
        avg_size_current = total_size_acc / 4.0
        self.ql_size.append(avg_size_current)

        # 5. Populate Feature Dictionary
        feats['disp'] = disp
        feats['acceleration_disp'] = accuracy
        feats['velocity_disp'] = self.ql_disp.get_mean()
        feats['velocity_size'] = self.ql_size.get_mean()
        feats['distance_cm'] = distance_cm

        # Update State
        self.old_coor = new_coor
        self.elapsed_frames += 1

        return self._pack_features(feats)

    def _pack_features(self, feats_dict):
        """Ensure consistent column order for the model."""
        # ORDER MUST MATCH TARGET_COLS in train_gpu.py
        return np.array([
            feats_dict.get('tip2dip', 0),
            feats_dict.get('tip2pip', 0),
            feats_dict.get('tip2mcp', 0),
            feats_dict.get('tip2wrist', 0),
            feats_dict.get('disp', 0),
            feats_dict.get('velocity_size', 0),
            feats_dict.get('velocity_disp', 0),
            feats_dict.get('acceleration_disp', 0),
            feats_dict.get('distance_cm', 0)
        ]).reshape(1, -1)
