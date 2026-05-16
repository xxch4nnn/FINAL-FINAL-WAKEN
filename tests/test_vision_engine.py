import unittest
from unittest.mock import MagicMock, patch
import sys

# Environment Mocking Strategy
mock_cv2 = MagicMock()
mock_mp = MagicMock()
mock_xgb = MagicMock()
mock_np = MagicMock()
mock_pygame = MagicMock()

sys.modules['cv2'] = mock_cv2
sys.modules['mediapipe'] = mock_mp
sys.modules['xgboost'] = mock_xgb
sys.modules['numpy'] = mock_np
sys.modules['pygame'] = mock_pygame

# Now we can safely import the module
from src.runtime.vision_engine import VisionEngine
from pathlib import Path

class TestVisionEngineSecurity(unittest.TestCase):
    @patch('src.runtime.vision_engine.Path.exists')
    @patch('src.runtime.vision_engine.xgb.XGBClassifier')
    def test_load_model_enforces_json_and_xgb(self, mock_xgb_classifier_cls, mock_exists):
        # Setup
        mock_exists.return_value = True
        mock_clf_instance = MagicMock()
        mock_xgb_classifier_cls.return_value = mock_clf_instance

        # Action
        engine = VisionEngine(model_path="models/some_model.pkl")

        # Assertions
        # 1. Verify XGBClassifier was used to load the model
        mock_xgb_classifier_cls.assert_called_once()

        # 2. Verify load_model was called
        mock_clf_instance.load_model.assert_called_once()

        # 3. Verify the path passed to load_model has the .json suffix
        called_path = mock_clf_instance.load_model.call_args[0][0]
        self.assertTrue(called_path.endswith('.json'))
        self.assertIn("some_model.json", called_path)

if __name__ == '__main__':
    unittest.main()
