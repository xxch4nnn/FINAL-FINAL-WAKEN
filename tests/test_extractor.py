import unittest
import numpy as np
import math
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy for missing mediapipe
sys.modules['mediapipe'] = MagicMock()
import mediapipe as mp

from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean_truncation(self):
        # Truncation logic testing dx = int(p1-p2)
        # Using arrays from _to_pixel logic which casts to int
        p1 = np.array([10.6, 20.9])
        p2 = np.array([5.1, 15.3])

        # In actual usage _to_pixel already gave ints:
        p1_int = np.array([10, 20])
        p2_int = np.array([5, 15])

        # Test basic mathematical correctness
        result = self.extractor._get_euclidean(p1_int, p2_int)
        expected = math.hypot(10-5, 20-15) # sqrt(5^2 + 5^2) = sqrt(50) = 7.071...
        self.assertAlmostEqual(result, expected)

    def test_get_euclidean_scalar_return_type(self):
        p1 = np.array([0, 0])
        p2 = np.array([3, 4])
        result = self.extractor._get_euclidean(p1, p2)
        self.assertEqual(result, 5.0)
        self.assertIsInstance(result, float) # math.hypot returns float

if __name__ == '__main__':
    unittest.main()
