## 2025-06-21 - OpenCV Text Readability Pattern
**Learning:** Text rendered using `cv2.putText` directly over dynamic video backgrounds is often unreadable due to color clashes and lack of contrast.
**Action:** All raw `cv2.putText` rendering over video frames must be wrapped with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA` to ensure legibility.
