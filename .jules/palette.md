## 2026-06-08 - OpenCV Text Readability Contrast
**Learning:** Raw `cv2.putText` text on dynamic video feeds often blends into the background, violating minimum WCAG color contrast guidelines and making real-time user feedback illegible.
**Action:** Always wrap text with a local `draw_text_with_outline` function to add a black stroke (thickness + 2) using `cv2.LINE_AA` for anti-aliasing.
