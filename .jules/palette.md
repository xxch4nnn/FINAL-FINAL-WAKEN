## 2024-05-24 - Accessibility and Readability Pattern in OpenCV UI
**Learning:** Raw `cv2.putText` overlaying a live camera feed can lead to severe legibility issues due to varying background colors and contrasts. OpenCV doesn't have a built-in text shadow/outline function.
**Action:** Always implement a `draw_text_with_outline` helper function (or similar strategy) drawing a thick dark stroke beneath the thin white text. Ensure keyboard accessibility/shortcuts are explicitly rendered on the UI.

## 2024-05-24 - explicit keyboard shortcut hints in OpenCV
**Learning:** Hard-to-discover keyboard shortcuts ('q', 'c', 'ESC') lead to a frustrating experience in a live vision application where standard UI buttons are absent.
**Action:** Explicitly render keyboard shortcut hints (e.g. `[Q] Quit`) at the top of the OpenCV window using `draw_text_with_outline` to improve discoverability without cluttering the center frame.
