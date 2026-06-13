## 2024-06-13 - OpenCV Text Readability over Dynamic Video
**Learning:** Raw text rendered using `cv2.putText` over a dynamic camera feed is often illegible due to lacking contrast against complex or matching backgrounds.
**Action:** Always wrap `cv2.putText` with a helper function like `draw_text_with_outline` that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`) behind the primary text using `cv2.LINE_AA` to ensure accessibility and readability.
