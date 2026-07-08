## 2024-07-08 - OpenCV Text Readability Pattern
**Learning:** Raw OpenCV text is frequently illegible against dynamic video backgrounds because the text color often blends with similar background pixel colors. Adding a contrasting outline is a critical accessibility improvement for heads-up displays.
**Action:** Always wrap `cv2.putText` with a helper function that draws a slightly thicker, contrasting (black) outline underneath the primary text to guarantee contrast ratio regardless of the background.
