import unittest
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()

from src.features.extractor import HandFeatureExtractor

class MockLandmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TestHandFeatureExtractor(unittest.TestCase):
    def test_euclidean_distance(self):
        extractor = HandFeatureExtractor(ref_width=1000, ref_height=1000)
        l1 = MockLandmark(0.1, 0.1)
        l2 = MockLandmark(0.4, 0.5)

        p1 = extractor._to_pixel(l1)
        p2 = extractor._to_pixel(l2)

        self.assertEqual(p1, (100, 100))
        self.assertEqual(p2, (400, 500))

        dist = extractor._get_euclidean(p1, p2)
        self.assertEqual(dist, 500.0)

if __name__ == '__main__':
    unittest.main()
