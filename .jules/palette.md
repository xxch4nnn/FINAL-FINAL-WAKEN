## 2026-07-03 - Improve Text Readability on Dynamic Backgrounds
**Learning:** Raw text rendered directly over a live video feed often becomes unreadable due to contrasting background colors and dynamic lighting.
**Action:** When using `cv2.putText` over dynamic video frames, always wrap the call to first render a thicker black outline (`thickness + 2`) behind the primary text to ensure consistent readability and contrast.
