## 2024-06-16 - Add Text Outline
**Learning:** Text rendered on dynamic video backgrounds is unreadable when drawn with just a single color (like `cv2.putText`). This is a critical accessibility issue because users cannot discern state changes or UI feedback if the video background color clashes with the text color.
**Action:** Always wrap `cv2.putText` with a helper function like `draw_text_with_outline` that first draws a thicker black stroke behind the text to ensure high contrast regardless of the background.
