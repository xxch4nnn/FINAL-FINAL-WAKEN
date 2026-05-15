import unittest
import numpy as np
import math
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean_integer_truncation(self):
        # The method should cast coordinate differences to int before squaring
        p1 = np.array([10.8, 20.2])
        p2 = np.array([5.1, 8.9])

        # Expected manual calculation with truncation
        dx = int(p1[0] - p2[0]) # int(10.8 - 5.1) = int(5.7) = 5
        dy = int(p1[1] - p2[1]) # int(20.2 - 8.9) = int(11.3) = 11
        expected = math.hypot(dx, dy)

        result = self.extractor._get_euclidean(p1, p2)

        self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
