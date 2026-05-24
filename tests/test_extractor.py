import sys
from unittest.mock import MagicMock

# Inject mock for mediapipe and cv2
sys.modules['mediapipe'] = MagicMock()
sys.modules['cv2'] = MagicMock()

import unittest
import numpy as np
import math
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def test_get_euclidean_truncation(self):
        extractor = HandFeatureExtractor()
        p1 = np.array([10.9, 20.8])
        p2 = np.array([5.1, 10.2])
        # Expected after truncation: dx=int(10.9-5.1)=int(5.8)=5, dy=int(20.8-10.2)=int(10.6)=10
        # -> math.hypot(5, 10)
        expected = math.hypot(5, 10)
        result = extractor._get_euclidean(p1, p2)
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
