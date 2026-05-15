import unittest
import sys
from unittest.mock import MagicMock

# Environment Mocking Strategy: Inject mocks into sys.modules BEFORE importing the module to test
sys.modules['mediapipe'] = MagicMock()
sys.modules['cv2'] = MagicMock()
# Since we need numpy for actual logic testing (e.g. np.array behavior), and it's installed via pip,
# we won't mock it. We only mock what's strictly missing.

import numpy as np

# Import the extractor after mocking the necessary dependencies
from src.features.extractor import HandFeatureExtractor

class TestHandFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HandFeatureExtractor()

    def test_get_euclidean_truncation(self):
        """
        Verify that _get_euclidean casts coordinate differences to int before squaring.
        This tests the truncation behavior specifically.
        """
        # Create float numpy arrays to simulate the input behavior before our int-cast inside _get_euclidean
        # Note: the actual input in the code is the output of `_to_pixel` which already casts to int.
        # But we still test the `_get_euclidean` function directly as per the requirement.
        p1 = np.array([10.9, 20.1])
        p2 = np.array([1.2, 5.8])

        # If dx = int(10.9 - 1.2) = int(9.7) = 9
        # dy = int(20.1 - 5.8) = int(14.3) = 14
        # expected = math.hypot(9, 14) = sqrt(81 + 196) = sqrt(277) = 16.6433...
        # Wait, inside _get_euclidean:
        # dx = int(p1[0] - p2[0]) -> int(10.9 - 1.2) = int(9.7) = 9
        # dy = int(p1[1] - p2[1]) -> int(20.1 - 5.8) = int(14.3) = 14
        # Wait, if p1[0] and p2[0] are float.
        # Let's test the logic.

        result = self.extractor._get_euclidean(p1, p2)

        # Expected calculation:
        expected_dx = int(p1[0] - p2[0])
        expected_dy = int(p1[1] - p2[1])
        import math
        expected_result = math.hypot(expected_dx, expected_dy)

        self.assertEqual(result, expected_result)

        # Verify it specifically truncated (9, 14) and not rounded/exact floats.
        self.assertEqual(expected_dx, 9)
        self.assertEqual(expected_dy, 14)

        # Another test case to be completely sure:
        p3 = np.array([5.9, 10.9])
        p4 = np.array([1.1, 1.1])
        # int(5.9 - 1.1) = int(4.8) = 4
        # int(10.9 - 1.1) = int(9.8) = 9
        # hypot(4, 9)

        result2 = self.extractor._get_euclidean(p3, p4)
        self.assertEqual(result2, math.hypot(4, 9))


if __name__ == '__main__':
    unittest.main()