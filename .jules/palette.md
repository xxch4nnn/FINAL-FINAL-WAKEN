## 2024-05-18 - High Contrast Discoverability
**Learning:** Text overlays on dynamic, variable-lighting camera feeds can fail WCAG contrast guidelines without a solid background or outline. Additionally, keyboard shortcuts for utility scripts must be persistently visible on-screen for discoverability.
**Action:** Always use a custom `draw_text_with_outline` helper for OpenCV text overlays to ensure readability against camera feeds, and explicitly render keyboard shortcuts at the top of the viewport (e.g., `(10, 30)`).
