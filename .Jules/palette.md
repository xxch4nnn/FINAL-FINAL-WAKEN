## 2024-10-24 - Text Contrast and Layout Overlap
**Learning:** Standard text overlays in OpenCV often fail WCAG contrast guidelines against dynamic, variable-lighting camera feeds. Additionally, adding top-anchored UI elements requires shifting existing ones down to avoid unreadable overlaps.
**Action:** Implemented a custom `draw_text_with_outline` helper locally in scripts and strictly adjusted Y-coordinates for overlapping elements.
