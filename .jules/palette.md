## 2024-05-24 - OpenCV Text Readability Pattern
**Learning:** Text rendered directly over dynamic video backgrounds (e.g. camera feeds in OpenCV) suffers from poor contrast depending on the underlying pixel colors, making it inaccessible or hard to read.
**Action:** Always wrap `cv2.putText` with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA` to ensure contrast regardless of background.
