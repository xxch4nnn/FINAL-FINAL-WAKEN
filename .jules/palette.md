## 2024-06-18 - Improve OpenCV Text Readability
**Learning:** Raw cv2.putText text rendered directly over dynamic video backgrounds is often unreadable due to contrasting background colors and patterns.
**Action:** Always wrap cv2.putText with a helper function that draws a thicker black stroke (color=(0, 0, 0), thickness + 2) behind the primary text using cv2.LINE_AA to ensure readability.
