## 2024-05-24 - OpenCV Text Legibility
**Learning:** Raw OpenCV text rendering lacks contrast against unpredictable live camera feeds. Text outlines (thick black stroke, thin fill) are essential for readability. Similarly, keybindings must be explicitly rendered on-screen to avoid hidden interactions.
**Action:** Always apply a 4px black stroke underneath a 2px fill color when using `cv2.putText` for UI text. Always include on-screen keyboard shortcut hints (e.g., `[ESC] Quit`).
