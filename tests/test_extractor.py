import unittest
import sys
from unittest.mock import MagicMock
import math

# Environment Mocking Strategy
sys.modules['mediapipe'] = MagicMock()
sys.modules['cv2'] = MagicMock()

import numpy as np
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean(self):
        # We simulate the inputs to _get_euclidean which are numpy arrays
        # The coordinates are expected to be pixels (already converted via _to_pixel)

        # Test 1: Standard integer-like floats that result from `_to_pixel`
        p1 = np.array([10.0, 20.0])
        p2 = np.array([13.0, 24.0])
        # Expected: dx = int(10-13) = -3, dy = int(20-24) = -4
        # math.hypot(-3, -4) = 5.0
        result = self.extractor._get_euclidean(p1, p2)
        self.assertEqual(result, 5.0)
        self.assertIsInstance(result, float)

        # Test 2: Verify truncation behavior for floating point inputs
        p1 = np.array([10.9, 20.9])
        p2 = np.array([13.1, 24.1])
        # Expected: dx = int(10.9 - 13.1) = int(-2.2) = -2
        # dy = int(20.9 - 24.1) = int(-3.2) = -3
        # math.hypot(-2, -3) = math.sqrt(4 + 9) = math.sqrt(13) = 3.605551275463989
        result = self.extractor._get_euclidean(p1, p2)
        expected = math.hypot(-2, -3)
        self.assertAlmostEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
