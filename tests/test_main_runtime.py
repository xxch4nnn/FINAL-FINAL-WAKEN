import unittest
from unittest.mock import MagicMock
import sys
import os
import json
import numpy as np

# Environment Mocking Strategy
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()

# Append root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main_runtime import JSONScaler

class TestJSONScaler(unittest.TestCase):
    def setUp(self):
        # Create dummy JSON scaler file for testing
        self.test_json_path = "test_scaler.json"
        dummy_data = {
            "mean_": [1.0, 2.0],
            "scale_": [0.5, 2.0]
        }
        with open(self.test_json_path, "w") as f:
            json.dump(dummy_data, f)

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.test_json_path):
            os.remove(self.test_json_path)

    def test_json_scaler_transform(self):
        scaler = JSONScaler(self.test_json_path)
        X = np.array([2.0, 6.0])

        # Expected: (X - mean) / scale
        # (2.0 - 1.0) / 0.5 = 2.0
        # (6.0 - 2.0) / 2.0 = 2.0
        expected = np.array([2.0, 2.0])

        result = scaler.transform(X)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
