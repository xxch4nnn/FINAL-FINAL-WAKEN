## 2024-05-24 - OpenCV Text Outline Pattern
**Learning:** Text rendered directly onto dynamic video frames lacks contrast, causing accessibility and readability issues. Outlining the text improves contrast and ensures it remains legible.
**Action:** Always wrap `cv2.putText` with a local `draw_text_with_outline` helper function using a thicker black stroke (`thickness + 2`, `cv2.LINE_AA`) behind the text in scripts rendering over dynamic backgrounds.
