import sys
from unittest.mock import MagicMock
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
import unittest
import numpy as np
import math
from src.features.extractor import HandFeatureExtractor

class MockLandmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_euclidean(self):
        p1 = np.array([100, 200])
        p2 = np.array([200, 400])
        dist = self.extractor._get_euclidean(p1, p2)
        # sqrt(100^2 + 200^2) = sqrt(10000 + 40000) = sqrt(50000)
        self.assertAlmostEqual(dist, math.sqrt(50000))

    def test_process_live_empty(self):
        self.assertIsNone(self.extractor.process_live([]))

    def test_process_live_valid(self):
        landmarks = [MockLandmark(np.random.rand(), np.random.rand()) for _ in range(21)]
        features = self.extractor.process_live(landmarks)
        self.assertIsNotNone(features)
        self.assertEqual(features.shape, (1, 9))

    def test_process_live_history(self):
        landmarks1 = [MockLandmark(np.random.rand(), np.random.rand()) for _ in range(21)]
        landmarks2 = [MockLandmark(np.random.rand(), np.random.rand()) for _ in range(21)]

        feat1 = self.extractor.process_live(landmarks1)
        feat2 = self.extractor.process_live(landmarks2)

        self.assertIsNotNone(feat1)
        self.assertIsNotNone(feat2)

if __name__ == '__main__':
    unittest.main()
