## 2024-06-23 - OpenCV Text Visibility Over Dynamic Backgrounds
**Learning:** Raw cv2.putText text rendering can be unreadable against dynamic video backgrounds.
**Action:** All raw cv2.putText text rendering over dynamic backgrounds must be wrapped with a local draw_text_with_outline helper function that first draws a thicker black stroke behind the primary text using cv2.LINE_AA.
