## 2024-05-24 - OpenCV Text Legibility
**Learning:** Raw OpenCV text (`cv2.putText`) can be hard to read against dynamic video backgrounds, making critical UI state unreadable.
**Action:** Wrap raw text rendering with a `draw_text_with_outline` local helper function that draws a thick black stroke behind the text.
