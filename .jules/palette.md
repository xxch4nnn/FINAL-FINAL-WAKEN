## 2024-07-06 - OpenCV Text Outline UX Pattern
**Learning:** Raw text rendered via `cv2.putText` over dynamic video backgrounds lacks sufficient contrast, leading to poor readability and accessibility issues for low-vision users.
**Action:** Implement a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA` to ensure sufficient contrast regardless of the background.
