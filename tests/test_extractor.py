import unittest
from src.features.extractor import HandFeatureExtractor
import numpy as np

class TestHandFeatureExtractor(unittest.TestCase):
    def test_euclidean(self):
        extractor = HandFeatureExtractor()
        p1 = np.array([10, 20])
        p2 = np.array([13, 24])

        # Original returns np.float64, math.hypot returns python float. Check they match.
        val = extractor._get_euclidean(p1, p2)
        self.assertAlmostEqual(val, 5.0)

if __name__ == '__main__':
    unittest.main()
