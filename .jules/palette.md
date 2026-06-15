## 2024-05-19 - Outline Text for OpenCV Readability
**Learning:** Raw `cv2.putText` text on dynamic video backgrounds is difficult to read. Wrapping text rendering with an outline (a thicker, black stroke) significantly improves contrast and accessibility for real-time video interfaces.
**Action:** Implement and use a `draw_text_with_outline` local helper function for OpenCV text overlays on dynamic backgrounds.
