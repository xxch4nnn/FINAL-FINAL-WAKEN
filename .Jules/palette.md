## 2024-04-01 - OpenCV UI Accessibility Pattern
**Learning:** Raw colored text overlaid on unpredictable live camera feeds using `cv2.putText` often suffers from poor legibility due to background interference. Furthermore, keyboard shortcuts are hidden unless explicitly drawn.
**Action:** Always use a "text outline" technique by drawing the same text first with a thicker black stroke (e.g., thickness=4) followed by the colored fill (thickness=2). Explicitly render essential keyboard shortcuts on-screen to improve interface discoverability.
