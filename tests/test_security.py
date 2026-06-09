import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()

class TestSecurityDeserialization(unittest.TestCase):
    def test_no_pickle_vision_engine(self):
        import src.runtime.vision_engine as ve
        with open(ve.__file__, 'r') as f:
            content = f.read()
        self.assertNotIn("import pickle", content)
        self.assertNotIn("pickle.load", content)

    def test_no_joblib_main_runtime(self):
        import main_runtime as mr
        with open(mr.__file__, 'r') as f:
            content = f.read()
        self.assertNotIn("import joblib", content)
        self.assertNotIn("joblib.load", content)

    def test_json_scaler(self):
        import main_runtime as mr
        import numpy as np
        scaler = mr.JSONScaler({'mean_': [1.0, 2.0], 'scale_': [2.0, 4.0]})
        res = scaler.transform([3.0, 10.0])
        np.testing.assert_array_equal(res, [1.0, 2.0])

if __name__ == '__main__':
    unittest.main()
