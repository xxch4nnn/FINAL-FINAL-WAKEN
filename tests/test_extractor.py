import unittest
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy
sys.modules['mediapipe'] = MagicMock()
sys.modules['cv2'] = MagicMock()

from src.features.extractor import HandFeatureExtractor
import numpy as np
import math

class TestHandFeatureExtractor(unittest.TestCase):
    def test_get_euclidean(self):
        extractor = HandFeatureExtractor()
        p1 = np.array([10, 20])
        p2 = np.array([13, 24])
        dist = extractor._get_euclidean(p1, p2)
        self.assertEqual(dist, 5.0)

    def test_get_euclidean_truncation(self):
        extractor = HandFeatureExtractor()
        # Test reference logic: int(p1[0]-p2[0])**2
        p1 = np.array([10.9, 20.9])
        p2 = np.array([13.1, 24.1])
        dist = extractor._get_euclidean(p1, p2)
        self.assertAlmostEqual(dist, math.sqrt(13), places=5)

if __name__ == '__main__':
    unittest.main()
