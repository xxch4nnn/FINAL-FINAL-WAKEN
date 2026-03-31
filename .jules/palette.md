## 2024-03-31 - OpenCV Text Contrast over Video
**Learning:** Standard colored text (like `cv2.putText` with just color) is completely inaccessible over unpredictable backgrounds like live video feeds, rendering UI elements unreadable depending on the camera angle or lighting.
**Action:** Always implement a text outline technique when rendering text over video feeds: draw a thick black stroke (e.g., thickness=4) first, followed by a thinner white/colored fill (e.g., thickness=2) to guarantee contrast ratio compliance regardless of the background.
