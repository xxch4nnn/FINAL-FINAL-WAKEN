import unittest
import numpy as np
import math
from src.features.extractor import HandFeatureExtractor
from collections import namedtuple

Landmark = namedtuple('Landmark', ['x', 'y'])

class TestExtractorPerformanceOpt(unittest.TestCase):
    def test_euclidean(self):
        extractor = HandFeatureExtractor()

        p1 = np.array([100, 200])
        p2 = np.array([150, 80])

        # Test original logic with math.hypot
        dx = int(p1[0] - p2[0])
        dy = int(p1[1] - p2[1])
        expected = np.sqrt(dx**2 + dy**2)

        actual = extractor._get_euclidean(p1, p2)

        self.assertAlmostEqual(actual, expected)
        # Should be a standard float due to math.hypot for scalar inputs
        self.assertIsInstance(actual, float)

if __name__ == '__main__':
    unittest.main()
