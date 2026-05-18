import sys
import unittest
from unittest.mock import MagicMock

# Environment Mocking Strategy
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['xgboost'] = MagicMock()

# Import after mocking
import numpy as np
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def test_get_euclidean(self):
        extractor = HandFeatureExtractor()
        p1 = np.array([10, 20])
        p2 = np.array([13, 24])
        # dx = -3, dy = -4 => sqrt(9 + 16) = 5.0
        result = extractor._get_euclidean(p1, p2)
        self.assertEqual(result, 5.0)

        # Test integer truncation behavior
        p3 = np.array([10.9, 20.9])
        p4 = np.array([13.1, 24.1])
        # p3[0]=10.9, p4[0]=13.1 => 10.9 - 13.1 = -2.2 -> int(-2.2) = -2
        # p3[1]=20.9, p4[1]=24.1 => 20.9 - 24.1 = -3.2 -> int(-3.2) = -3
        # sqrt(4 + 9) = sqrt(13) = 3.605551275463989
        result_trunc = extractor._get_euclidean(p3, p4)
        self.assertAlmostEqual(result_trunc, 3.605551275463989)
