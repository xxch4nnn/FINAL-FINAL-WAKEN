## 2024-03-28 - [Text Legibility on Live Camera Feeds]
**Learning:** Text rendered directly over a live camera feed can easily become unreadable due to unpredictable background colors and lighting changes.
**Action:** Always use a 'text outline' technique when using `cv2.putText` (draw a thick black stroke followed by a thin colored fill) to ensure contrast and legibility regardless of the background.
