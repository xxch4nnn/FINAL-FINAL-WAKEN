## 2024-04-24 - OpenCV UI Contrast and Discoverability
**Learning:** Raw `cv2.putText` is often unreadable against live, unpredictable camera backgrounds, causing poor accessibility. Additionally, console-only keybindings are undiscoverable, trapping users.
**Action:** Always implement a text outline approach (thick black base + thin colored fill) for OpenCV UI elements. Always explicitly render keyboard hints (e.g., `[Q] Quit`) directly on the video frame, preferably at the top to avoid overlap with hand tracking interaction zones.
