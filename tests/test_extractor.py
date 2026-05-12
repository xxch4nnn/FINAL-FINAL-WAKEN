import unittest
import numpy as np
import math

from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean_correctness_and_truncation(self):
        # We test that the truncation works correctly and it outputs the expected value
        p1 = np.array([10.8, 20.2])
        p2 = np.array([5.1, 8.9])

        # Original logic: int(10.8 - 5.1) = int(5.7) = 5
        # int(20.2 - 8.9) = int(11.3) = 11
        # math.hypot(5, 11) = sqrt(25 + 121) = sqrt(146) = 12.083045973594572

        expected_distance = math.hypot(5, 11)
        calculated_distance = self.extractor._get_euclidean(p1, p2)

        # We assert that calculated_distance matches expected_distance
        self.assertAlmostEqual(calculated_distance, expected_distance, places=5)

if __name__ == '__main__':
    unittest.main()
