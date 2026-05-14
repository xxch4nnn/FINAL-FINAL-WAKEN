## 2024-05-15 - High-Contrast Text and Discoverable Shortcuts
**Learning:** Dynamic, variable-lighting camera feeds make standard text overlays unreadable. Users also lack discoverability for script-specific keyboard shortcuts.
**Action:** Implemented `draw_text_with_outline` for WCAG-compliant contrast and persistently render keyboard shortcuts at the top of the viewport `(10, 30)`.
