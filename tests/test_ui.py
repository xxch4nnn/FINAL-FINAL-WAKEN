import sys
from unittest.mock import MagicMock

sys.modules['cv2'] = MagicMock()
sys.modules['numpy'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pygame'] = MagicMock()
sys.modules['joblib'] = MagicMock()
sys.modules['scipy'] = MagicMock()
sys.modules['scipy.signal'] = MagicMock()

import main_runtime
import VisionEngine

def test_draw_text_with_outline_main_runtime():
    img = MagicMock()
    # Reset mock since the module might have called it during import
    main_runtime.cv2.putText.reset_mock()
    main_runtime.draw_text_with_outline(img, "test", (0, 0), 0, 1.0, (255, 255, 255), 1)
    assert main_runtime.cv2.putText.call_count == 2
    print("main_runtime test passed")

def test_draw_text_with_outline_vision_engine():
    img = MagicMock()
    # Reset mock since the module might have called it during import
    VisionEngine.cv2.putText.reset_mock()
    VisionEngine.draw_text_with_outline(img, "test", (0, 0), 0, 1.0, (255, 255, 255), 1)
    assert VisionEngine.cv2.putText.call_count == 2
    print("VisionEngine test passed")

if __name__ == "__main__":
    test_draw_text_with_outline_main_runtime()
    test_draw_text_with_outline_vision_engine()
