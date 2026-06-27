## 2024-06-27 - OpenCV Text Contrast
**Learning:** Raw `cv2.putText` text on dynamic video backgrounds is difficult to read. The codebase requires an OpenCV UX Pattern where all raw text is wrapped in a `draw_text_with_outline` local helper function.
**Action:** Implemented the local helper and updated all `cv2.putText` calls to use the outline function in `main_runtime.py` and `VisionEngine.py`.
