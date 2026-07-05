## 2026-07-05 - OpenCV Text Legibility
**Learning:** Raw OpenCV text (`cv2.putText`) is often unreadable against dynamic video backgrounds due to lack of contrast.
**Action:** Always wrap text rendering with a `draw_text_with_outline` helper function that adds a thicker black stroke (`cv2.LINE_AA`) behind the primary text for all dynamic video scripts.
