import unittest
import math
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy for mediapipe and cv2
sys.modules['mediapipe'] = MagicMock()
sys.modules['cv2'] = MagicMock()

from src.features.extractor import HandFeatureExtractor

class TestExtractor(unittest.TestCase):
    def test_get_euclidean(self):
        extractor = HandFeatureExtractor()
        # Using simple lists which act like the numpy arrays returned by _to_pixel
        p1 = [10.5, 20.2]
        p2 = [0, 0]
        # Extractor truncates to int before squaring, so it will be 10 and 20.
        dist = extractor._get_euclidean(p1, p2)
        self.assertAlmostEqual(dist, 22.360679774997898)

if __name__ == '__main__':
    unittest.main()
