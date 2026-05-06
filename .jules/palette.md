## 2024-05-06 - [High-Contrast Text Overlays]
**Learning:** Standard OpenCV `cv2.putText` overlays fail WCAG contrast guidelines when rendered against dynamic, variable-lighting camera feeds, making the UI inaccessible or difficult to read. In addition, hidden keyboard shortcuts frustrate users by lacking discoverability.
**Action:** Introduced a reusable `draw_text_with_outline` function across all vision scripts to render a black outline behind text, ensuring readability. Also persistently displayed keyboard shortcut hints at the top of the viewport (10, 30).
