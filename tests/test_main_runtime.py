import unittest
from unittest.mock import MagicMock
import sys

# Environment Mocking Strategy
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['joblib'] = MagicMock()
sys.modules['scipy'] = MagicMock()
sys.modules['scipy.signal'] = MagicMock()

import numpy as np
from main_runtime import get_hand_in_aruco_space

class TestMainRuntime(unittest.TestCase):
    def test_get_hand_in_aruco_space(self):
        # We simulate hand_norm = [0.5, 0.5]
        hand_norm = np.array([0.5, 0.5])

        # Identity K (Width 1000, Height 1000)
        # cx = 500, cy = 500
        K = np.array([[1000, 0, 500], [0, 1000, 500], [0, 0, 1]], dtype=np.float32)
        D = np.zeros((4,1))

        # rvec and tvec to place marker at (0,0,1) with identity rotation
        rvec = np.zeros((3,1))
        tvec = np.array([[0], [0], [1.0]])

        # cv2.Rodrigues needs to be mocked specifically because get_hand_in_aruco_space calls it
        sys.modules['cv2'].Rodrigues.return_value = (np.eye(3), None)

        # For x_ray = (u - cx)/fx = (500-500)/1000 = 0
        # Ray = [0, 0, 1]
        # P_aruco.z = 0.
        # ray_cam = R * P_aruco + t
        # R = I, t = [0,0,1].
        # lambda * [0, 0, 1] = [x_a, y_a, 0] + [0, 0, 1]
        # lambda = 1. x_a = 0, y_a = 0

        x_aruco = get_hand_in_aruco_space(hand_norm, rvec, tvec, K, D)

        self.assertIsNotNone(x_aruco)
        self.assertAlmostEqual(x_aruco, 0.14, places=2)

if __name__ == '__main__':
    unittest.main()
