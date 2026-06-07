import unittest
from src.features.extractor import HandFeatureExtractor

class DummyLandmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TestExtractor(unittest.TestCase):
    def test_process_live(self):
        extractor = HandFeatureExtractor()
        lms1 = [DummyLandmark(0.1, 0.1)] * 21
        lms1[0] = DummyLandmark(0.1, 0.1)
        lms1[5] = DummyLandmark(0.2, 0.2)
        lms1[6] = DummyLandmark(0.3, 0.3)
        lms1[7] = DummyLandmark(0.4, 0.4)
        lms1[8] = DummyLandmark(0.5, 0.5)
        feats1 = extractor.process_live(lms1)
        self.assertIsNotNone(feats1)

        lms2 = [DummyLandmark(0.1, 0.1)] * 21
        lms2[0] = DummyLandmark(0.1, 0.1)
        lms2[5] = DummyLandmark(0.2, 0.2)
        lms2[6] = DummyLandmark(0.3, 0.3)
        lms2[7] = DummyLandmark(0.4, 0.4)
        lms2[8] = DummyLandmark(0.6, 0.6)
        feats2 = extractor.process_live(lms2)
        self.assertIsNotNone(feats2)
        self.assertEqual(len(extractor.history), 2)
if __name__ == '__main__':
    unittest.main()
