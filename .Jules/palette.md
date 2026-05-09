## 2024-05-08 - WCAG Text Contrast in Dynamic Backgrounds
**Learning:** Standard UI text (like `cv2.putText`) fails WCAG contrast guidelines when placed over variable-lighting camera feeds in real-time computer vision applications. Users could not read state information or discover keyboard shortcuts.
**Action:** Replaced standard text rendering with a custom `draw_text_with_outline` helper that paints a solid black stroke behind all text, ensuring readable contrast against any background color or lighting condition. Explicitly listed UI controls on-screen so they are discoverable.
