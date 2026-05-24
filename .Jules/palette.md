## 2024-05-24 - Custom Text Outline for High Contrast
**Learning:** In computer vision applications with dynamic camera feeds, standard text overlays (`cv2.putText`) often suffer from poor contrast against varying backgrounds, reducing accessibility.
**Action:** Implement a custom `draw_text_with_outline` utility that renders a black outline behind text overlays to guarantee readability regardless of lighting or background, as per WCAG contrast guidelines.
