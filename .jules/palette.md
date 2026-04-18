## 2024-04-18 - High-Contrast UI Text and Discoverability
**Learning:** Standard OpenCV `cv2.putText` lacks contrast against varied live camera feeds, making UI elements unreadable depending on the background. Additionally, missing visible keyboard shortcuts hinders discoverability.
**Action:** Always use a 'text outline' technique (draw thick black stroke, then thin colored/white fill) for `cv2.putText` and explicitly render keybindings on-screen.
