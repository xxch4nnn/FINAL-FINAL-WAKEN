## 2024-05-24 - OpenCV UI Legibility
**Learning:** Raw colored text overlaid on live camera feeds often becomes unreadable against unpredictable backgrounds (e.g., bright windows, colorful clothing).
**Action:** Always employ a text-outline technique when using `cv2.putText` by drawing a thick black stroke (e.g., `thickness=4`) followed by the thinner primary text (e.g., `thickness=2`).
