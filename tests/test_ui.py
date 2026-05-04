import unittest
import sys
from unittest.mock import MagicMock, call
import numpy as np

# Environment Mocking Strategy
sys.modules['cv2'] = MagicMock()
sys.modules['cv2.aruco'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()

# Import the target module
from main_runtime import draw_text_with_outline
import cv2

class TestUIHelpers(unittest.TestCase):
    def setUp(self):
        cv2.putText.reset_mock()

    def test_draw_text_with_outline(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        text = "Test"
        pos = (10, 20)
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 1.0
        color = (255, 255, 255)
        thickness = 2

        draw_text_with_outline(img, text, pos, font, scale, color, thickness)

        # Assert cv2.putText was called 2 times (outline + text)
        self.assertEqual(cv2.putText.call_count, 2)

if __name__ == '__main__':
    unittest.main()
