## 2025-05-28 - Camera Feed Text Contrast & Shortcut Discoverability
**Learning:** Raw colored text overlaid on dynamic camera feeds often fails WCAG contrast guidelines due to unpredictable lighting and background colors. Additionally, invisible keyboard shortcuts frustrate users who don't know the controls.
**Action:** Always implement a `draw_text_with_outline` helper to ensure text legibility against any background, and persistently display available keyboard shortcuts at the top of the viewport (e.g., `(10, 30)`).
