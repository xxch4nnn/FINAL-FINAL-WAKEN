## 2024-06-11 - OpenCV Text Readability
**Learning:** Raw `cv2.putText` text rendering over dynamic video backgrounds is often unreadable due to lack of contrast.
**Action:** Always wrap `cv2.putText` with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA` to ensure text is legible against dynamic video backgrounds. Do not apply this to scripts rendering static images.
