## 2024-05-24 - [High-Contrast Text over Video Feeds]
**Learning:** Standard text rendered via `cv2.putText` over raw camera feeds frequently suffers from poor contrast and legibility, especially when the background color matches the text color.
**Action:** Always implement a "text outline" technique (drawing a thicker black stroke underneath a thinner white fill) for critical UI elements and explicitly render keyboard shortcuts to improve interface discoverability and accessibility.
