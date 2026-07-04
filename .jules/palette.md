## 2023-10-27 - Text Outlines for Video Readability
**Learning:** Raw `cv2.putText` text rendering is often illegible against dynamic video backgrounds because the text color may blend with the background pixels.
**Action:** All raw `cv2.putText` rendering on video frames must be wrapped with a local `draw_text_with_outline` helper function that draws a thicker black stroke behind the text to ensure contrast and readability.
