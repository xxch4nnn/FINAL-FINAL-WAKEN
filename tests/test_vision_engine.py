import sys
from unittest.mock import MagicMock
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()

import unittest
from unittest.mock import patch
from src.runtime.vision_engine import VisionEngine

class TestVisionEngineSecurity(unittest.TestCase):
    @patch('src.runtime.vision_engine.Path.exists')
    def test_load_model_secure_path(self, mock_exists):
        mock_exists.return_value = True
        engine = VisionEngine(model_path="models/rf_model.pkl")
        xgb_mock = sys.modules['xgboost']
        xgb_mock.XGBClassifier().load_model.assert_called_with("models/rf_model.json")

if __name__ == '__main__':
    unittest.main()
