import unittest
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy
sys.modules['mediapipe'] = MagicMock()

from src.features.extractor import HandFeatureExtractor

class TestExtractor(unittest.TestCase):
    def test_get_euclidean_truncation(self):
        extractor = HandFeatureExtractor()
        # p1 and p2 as arrays with floating-point values
        p1 = [10.8, 20.9]
        p2 = [5.1, 10.2]

        # In `_get_euclidean`, it should cast to int:
        # dx = int(10.8 - 5.1) = int(5.7) = 5
        # dy = int(20.9 - 10.2) = int(10.7) = 10
        # distance = math.hypot(5, 10) = sqrt(25 + 100) = sqrt(125) ≈ 11.180339887498949

        expected_distance = (5**2 + 10**2)**0.5
        result = extractor._get_euclidean(p1, p2)

        self.assertAlmostEqual(result, expected_distance)

if __name__ == '__main__':
    unittest.main()