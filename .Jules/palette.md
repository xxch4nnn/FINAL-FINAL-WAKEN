## 2024-05-24 - Accessibility: Text Contrast & Discoverability
**Learning:** Standard text overlays in dynamic camera feeds often suffer from poor contrast, and hidden keyboard shortcuts reduce accessibility.
**Action:** Ensure all text overlays use a custom `draw_text_with_outline` function (drawing a black background outline) to meet WCAG contrast guidelines against any background, and persistently render available keyboard shortcuts at the top of the viewport.
