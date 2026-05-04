import unittest
import numpy as np
import math
import time
from src.features.extractor import HandFeatureExtractor

class TestExtractor(unittest.TestCase):
    def test_euclidean(self):
        ex = HandFeatureExtractor()
        p1 = np.array([10, 20])
        p2 = np.array([5, 10])
        dist = ex._get_euclidean(p1, p2)
        # Verify it calculates correctly
        self.assertAlmostEqual(dist, math.hypot(5, 10))

if __name__ == '__main__':
    unittest.main()
