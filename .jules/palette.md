## 2024-04-10 - High Contrast Text Overlays in CV Pipelines
**Learning:** Raw OpenCV text overlay `cv2.putText` on unpredictable live camera feeds often results in unreadable HUD elements due to low contrast against varied backgrounds. This negatively impacts accessibility and user experience.
**Action:** Always implement a `draw_text_with_outline` utility (drawing a thick black stroke followed by a thinner white/colored fill) when rendering dynamic UI elements over video streams to ensure contrast accessibility standards.

## 2024-04-10 - Keyboard Shortcut Discoverability in Headless/CV UIs
**Learning:** CV applications that rely on standard OpenCV windows (`cv2.imshow`) lack native menus, causing hidden "magic keys" (e.g., 'q' to quit, 'c' to calibrate) to be completely undiscoverable by the end-user.
**Action:** Always explicitly render critical keyboard shortcuts on the HUD (e.g., `[q] Quit | [c] Calibrate`) using outlined text to improve interaction discoverability and prevent user lock-in.
