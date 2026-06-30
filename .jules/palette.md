## 2024-05-24 - OpenCV Readability over Video Backgrounds
**Learning:** Raw text rendered via `cv2.putText` over dynamic, fast-moving video streams suffers from severe readability issues due to color blending and lack of contrast.
**Action:** Always wrap text rendering with a `draw_text_with_outline` helper function that adds a thick `cv2.LINE_AA` black stroke behind the primary text for clear legibility regardless of the video background.
