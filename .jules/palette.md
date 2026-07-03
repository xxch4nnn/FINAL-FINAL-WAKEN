## 2026-07-02 - Text Readability on Dynamic Backgrounds
**Learning:** Raw OpenCV text rendering (`cv2.putText`) often lacks contrast against dynamic video backgrounds, making UI elements unreadable and failing accessibility standards.
**Action:** Always wrap `cv2.putText` with a local `draw_text_with_outline` helper function that draws a thick black stroke behind the primary text to ensure contrast and readability in high-frequency CV loops.
