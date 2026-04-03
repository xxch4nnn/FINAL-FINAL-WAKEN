## 2024-05-24 - OpenCV Camera UI Discoverability and Contrast
**Learning:** Text overlaid on noisy camera feeds without a contrasting stroke is often illegible, creating accessibility barriers. Additionally, since the UI captures full keyboard focus, users often struggle to find the correct exit keys (like 'q' or 'ESC') without explicit visual hints.
**Action:** Always apply the "text outline" pattern (thick dark stroke under thin light text) when using `cv2.putText` over camera feeds, and explicitly render critical keyboard shortcuts on the screen to improve discoverability.
