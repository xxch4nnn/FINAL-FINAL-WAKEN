import unittest
import numpy as np
from src.features.extractor import HandFeatureExtractor
import math

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean_int_truncation(self):
        # Testing integer truncation logic described in memory
        # e.g., difference is floating point, but dx/dy should be int
        p1 = np.array([10.5, 20.8])
        p2 = np.array([7.1, 16.3])

        # dx = int(10.5 - 7.1) = int(3.4) = 3
        # dy = int(20.8 - 16.3) = int(4.5) = 4
        # Expected distance: math.hypot(3, 4) = 5.0
        dist = self.extractor._get_euclidean(p1, p2)

        self.assertEqual(dist, 5.0)

    def test_get_euclidean_zeros(self):
        p1 = np.array([0, 0])
        p2 = np.array([0, 0])
        self.assertEqual(self.extractor._get_euclidean(p1, p2), 0.0)

    def test_get_euclidean_negative_diffs(self):
        p1 = np.array([-5, -5])
        p2 = np.array([1, 3])
        # dx = int(-5 - 1) = -6
        # dy = int(-5 - 3) = -8
        # dist = math.hypot(-6, -8) = 10.0
        self.assertEqual(self.extractor._get_euclidean(p1, p2), 10.0)

if __name__ == '__main__':
    unittest.main()
