import unittest
import numpy as np
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean(self):
        # The prompt explicitly requires that we verify the int truncation behavior
        # Reference logic casts to int before squaring
        # Let's test with float arrays
        p1 = np.array([10.6, 20.9])
        p2 = np.array([5.2, 8.1])

        # dx = int(10.6 - 5.2) = int(5.4) = 5
        # dy = int(20.9 - 8.1) = int(12.8) = 12
        # sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.0
        result = self.extractor._get_euclidean(p1, p2)

        self.assertEqual(result, 13.0)

if __name__ == '__main__':
    unittest.main()
