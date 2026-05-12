## 2026-05-12 - Persistent Text Outlines for Accessibility
**Learning:** Raw colored text drawn with `cv2.putText` over dynamic camera feeds often fails WCAG contrast guidelines due to unpredictable backgrounds. Furthermore, shortcut keys should be persistent and easily discoverable.
**Action:** Implement `draw_text_with_outline` in runtime visualizers to provide a high-contrast black border behind text, ensuring readability against any background. Always draw discoverable keyboard shortcuts using this method.
