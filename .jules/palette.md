## 2024-06-18 - Improve Text Readability against Dynamic Backgrounds
**Learning:** Raw text rendered over live video feeds often suffers from poor contrast and readability due to varying background colors and lighting conditions.
**Action:** Always wrap `cv2.putText` rendering with a `draw_text_with_outline` helper function that first draws a thick black stroke behind the text to ensure constant contrast regardless of the background.
