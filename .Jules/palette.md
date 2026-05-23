## 2024-05-23 - Text Contrast on Dynamic Backgrounds
**Learning:** Standard text overlays in computer vision applications (like `cv2.putText`) often fail WCAG contrast guidelines when placed over variable-lighting camera feeds, making the UI inaccessible or difficult to read for many users.
**Action:** Implemented a custom `draw_text_with_outline` function to add a black outline behind text across the application, ensuring readability regardless of the background pixels. This pattern should be standard for all live camera UI elements.
