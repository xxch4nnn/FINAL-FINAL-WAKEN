import unittest
import numpy as np
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def test_get_euclidean_truncates_to_int(self):
        extractor = HandFeatureExtractor()

        # Points with fractional parts that would round up if rounded normally,
        # but should be truncated if cast to int.
        # e.g., 10.9 -> 10, 5.8 -> 5. diff is 5.
        p1 = np.array([10.9, 20.8])
        p2 = np.array([5.1, 8.2])

        # Expected:
        # dx = int(10.9 - 5.1) = int(5.8) = 5
        # dy = int(20.8 - 8.2) = int(12.6) = 12
        # dist = sqrt(5**2 + 12**2) = sqrt(25 + 144) = sqrt(169) = 13.0

        expected_dist = 13.0
        actual_dist = extractor._get_euclidean(p1, p2)

        self.assertAlmostEqual(actual_dist, expected_dist, places=5)

if __name__ == '__main__':
    unittest.main()
