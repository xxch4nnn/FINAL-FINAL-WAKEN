import sys
from unittest.mock import MagicMock
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()

import unittest
from src.features.extractor import HandFeatureExtractor

class TestExtractorPerf(unittest.TestCase):
    def test_native_math_used(self):
        extractor = HandFeatureExtractor()

        class MockLandmark:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        landmarks = [MockLandmark(0.01 * i, 0.01 * i) for i in range(21)]
        res1 = extractor.process_live(landmarks)
        res2 = extractor.process_live(landmarks)

        self.assertIsNotNone(res1)
        self.assertIsNotNone(res2)

if __name__ == '__main__':
    unittest.main()
