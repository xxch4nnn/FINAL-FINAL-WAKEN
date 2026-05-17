## 2024-05-17 - Text Contrast on Dynamic Camera Backgrounds
**Learning:** Raw colored text (e.g., `cv2.putText` with bright green/red) fails WCAG contrast guidelines against dynamic, unpredictable lighting in live camera feeds, making status indicators unreadable for visually impaired users or in suboptimal lighting conditions.
**Action:** Implement and standardize a `draw_text_with_outline` utility function across all vision scripts to render a high-contrast black outline behind all text overlays, ensuring readability regardless of background pixel values.

## 2024-05-17 - Keyboard Shortcut Discoverability
**Learning:** Users lack awareness of essential interactive controls (like pressing 'c' for calibration or 'q' to quit) when running the script directly from the terminal, as they are not visible in the UI itself.
**Action:** Render critical keyboard shortcuts persistently in the top-left viewport corner `(10, 30)`, ensuring existing elements (like the state display) are vertically displaced to avoid overlapping.