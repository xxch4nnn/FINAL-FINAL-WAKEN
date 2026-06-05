import unittest
import sys
from unittest.mock import MagicMock

sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()

from main_runtime import JSONScaler
import numpy as np
import json
import tempfile

class TestSecurity(unittest.TestCase):
    def test_json_scaler(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({'mean_': [1.0], 'scale_': [2.0]}, f)
            tmp_name = f.name

        scaler = JSONScaler(tmp_name)
        res = scaler.transform([[3.0]])
        self.assertEqual(res[0][0], 1.0)

if __name__ == '__main__':
    unittest.main()
