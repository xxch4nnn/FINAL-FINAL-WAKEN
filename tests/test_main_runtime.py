import unittest
import sys
from unittest.mock import MagicMock, patch
import json
import numpy as np

# Mock heavy dependencies before import
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()

import main_runtime

class TestJSONScaler(unittest.TestCase):
    def test_json_scaler_transform(self):
        data = {
            "mean_": [1.0, 2.0],
            "scale_": [2.0, 4.0]
        }
        scaler = main_runtime.JSONScaler(data)
        X = [[3.0, 10.0]]
        result = scaler.transform(X)
        np.testing.assert_array_almost_equal(result, [[1.0, 2.0]])

    def test_json_scaler_empty(self):
        scaler = main_runtime.JSONScaler({})
        X = [[3.0, 10.0]]
        result = scaler.transform(X)
        # Should return unscaled
        np.testing.assert_array_almost_equal(result, [[3.0, 10.0]])

if __name__ == '__main__':
    unittest.main()
