import sys
import unittest.mock

# Mock dependencies
sys.modules['mediapipe'] = unittest.mock.MagicMock()
sys.modules['numpy'] = unittest.mock.MagicMock()

from src.features.extractor import HandFeatureExtractor

class DummyLandmark:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

# Mock 21 landmarks
landmarks = [DummyLandmark(0.1, 0.1) for _ in range(21)]

extractor = HandFeatureExtractor()

# Test process_live
features1 = extractor.process_live(landmarks)
features2 = extractor.process_live(landmarks)

print("Features extracted successfully:", features2 is not None)
print(features2)