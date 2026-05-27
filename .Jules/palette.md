## 2024-05-24 - High Contrast Text Overlays for Camera Feeds
**Learning:** Raw text overlays on dynamic, variable-lighting camera feeds frequently fail WCAG contrast guidelines, making UI elements unreadable.
**Action:** Always use a custom `draw_text_with_outline` function that renders a black outline behind the text to guarantee contrast against any background in OpenCV applications.
