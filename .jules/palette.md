## 2025-01-20 - OpenCV Text Contrast
**Learning:** Raw `cv2.putText` rendering is unreadable against dynamic video backgrounds.
**Action:** All raw `cv2.putText` text rendering must be wrapped with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA`.
