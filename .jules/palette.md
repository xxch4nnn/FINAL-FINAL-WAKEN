## 2024-06-29 - Text Readability on Dynamic Backgrounds
**Learning:** OpenCV's default text rendering (`cv2.putText`) often blends into dynamic video backgrounds, making it hard to read and reducing accessibility.
**Action:** Always wrap text rendered over dynamic video backgrounds with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA`.
