## 2024-05-25 - Improve Text Contrast and Discoverability
**Learning:** Unoutlined text overlays on dynamic camera feeds fail WCAG contrast guidelines, making the UI inaccessible under varying lighting conditions. Additionally, hidden keyboard shortcuts severely reduce discoverability.
**Action:** Implement `draw_text_with_outline` for all OpenCV text rendering to ensure constant contrast against any background, and persistently display available keyboard shortcuts at `(10, 30)` on all viewports to improve accessibility without shifting existing elements.
