## 2024-05-18 - Text Contrast and Keyboard Shortcuts
**Learning:** Raw `cv2.putText` on live camera feeds often suffers from poor legibility due to unpredictable background colors and brightness. Additionally, hidden keyboard shortcuts (like `q` to quit or `c` to calibrate) frustrate users who must guess or consult documentation.
**Action:** Always implement a text outline approach (thick black stroke beneath thin white fill) for OpenCV UI overlays. Explicitly render essential keyboard shortcuts on-screen at consistent locations (e.g., top-left) to improve interface discoverability.
