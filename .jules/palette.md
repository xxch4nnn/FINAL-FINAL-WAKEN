## 2024-05-31 - High Contrast Text for Dynamic Backgrounds
**Learning:** Rendering text over dynamic camera backgrounds using `cv2.putText` often violates WCAG contrast guidelines because the text color can blend with similar background colors, making the UI inaccessible or hard to read.
**Action:** Added a custom `draw_text_with_outline` function that draws a black stroke behind the text to ensure high contrast against any background color across `main_runtime.py`, `VisionEngine.py`, and `src/runtime/vision_engine.py`.
