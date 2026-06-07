## 2024-05-23 - Text Outline
**Learning:** OpenCV text without an outline is illegible against dynamic video backgrounds.
**Action:** Always wrap `cv2.putText` with a helper function that draws a black outline.
