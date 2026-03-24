## 2024-03-24 - OpenCV Text Legibility
**Learning:** Raw colored text drawn with `cv2.putText` can be difficult to read against dynamic, unpredictable live camera feeds, creating accessibility issues.
**Action:** Always use the 'text outline' technique when drawing text on camera feeds: draw a thick black stroke (e.g., `color=(0,0,0)`, `thickness=4`) followed by the original thin colored/white fill (e.g., `thickness=2`).
