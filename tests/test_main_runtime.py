import unittest
import numpy as np
import sys
from unittest.mock import MagicMock

sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()

import main_runtime

class TestMainRuntime(unittest.TestCase):
    def test_get_hand_in_aruco_space_returns_none_on_missing_args(self):
        hand_norm = np.array([0.5, 0.5])
        K = np.eye(3)
        D = np.zeros(4)

        # Expected behavior: returns None
        result = main_runtime.get_hand_in_aruco_space(hand_norm, None, np.zeros(3), K, D)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
