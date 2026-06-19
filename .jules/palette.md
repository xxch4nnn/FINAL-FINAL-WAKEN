## 2024-10-24 - [OpenCV Text Readability]
**Learning:** Raw `cv2.putText` is often unreadable against dynamic video backgrounds because the text color can blend with the background pixels, causing accessibility issues.
**Action:** All text rendered over video streams must be wrapped with a `draw_text_with_outline` helper that first draws a thicker black stroke behind the primary text using `cv2.LINE_AA` to ensure contrast and readability in all lighting conditions.
