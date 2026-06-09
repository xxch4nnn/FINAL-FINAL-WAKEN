import sys
from unittest.mock import MagicMock
import unittest

sys.modules['cv2'] = MagicMock()
sys.modules['numpy'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()
sys.modules['joblib'] = MagicMock()
sys.modules['scipy.signal'] = MagicMock()

import main_runtime
import VisionEngine

class TestUIHelpers(unittest.TestCase):
    def test_draw_text_with_outline_main(self):
        img_mock = MagicMock()
        main_runtime.draw_text_with_outline(img_mock, "Test", (0, 0), 1, 1.0, (255, 255, 255), 1)
        self.assertEqual(sys.modules['cv2'].putText.call_count, 2)
        sys.modules['cv2'].putText.reset_mock()

    def test_draw_text_with_outline_vision(self):
        img_mock = MagicMock()
        VisionEngine.draw_text_with_outline(img_mock, "Test", (0, 0), 1, 1.0, (255, 255, 255), 1)
        self.assertEqual(sys.modules['cv2'].putText.call_count, 2)
        sys.modules['cv2'].putText.reset_mock()

if __name__ == '__main__':
    unittest.main()
