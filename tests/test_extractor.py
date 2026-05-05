import unittest
import numpy as np
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def test_get_euclidean_truncation(self):
        extractor = HandFeatureExtractor()

        # Test 1: Simple integer coordinates
        p1 = np.array([10.0, 20.0])
        p2 = np.array([5.0, 8.0])
        self.assertEqual(extractor._get_euclidean(p1, p2), 13.0)  # sqrt(5^2 + 12^2) = 13.0

        # Test 2: Floating point inputs that require truncation
        # With int cast: dx = int(10.8 - 5.1) = int(5.7) = 5
        # With int cast: dy = int(20.9 - 8.2) = int(12.7) = 12
        # Result should be exactly 13.0
        p3 = np.array([10.8, 20.9])
        p4 = np.array([5.1, 8.2])
        self.assertEqual(extractor._get_euclidean(p3, p4), 13.0)

        # Test 3: Without int cast, the distance would be approx 13.9
        # This test ensures the integer truncation happens *before* squaring
        p5 = np.array([10.9, 20.9])
        p6 = np.array([5.0, 8.0])
        # dx = int(5.9) = 5
        # dy = int(12.9) = 12
        # Expected: 13.0
        self.assertEqual(extractor._get_euclidean(p5, p6), 13.0)

if __name__ == '__main__':
    unittest.main()
