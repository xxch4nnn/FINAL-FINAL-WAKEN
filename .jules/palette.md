## 2024-06-25 - OpenCV Text Legibility
**Learning:** Raw OpenCV text (`cv2.putText`) on dynamic video backgrounds is often unreadable due to contrasting colors blending with the moving image. A black stroke/outline provides essential contrast.
**Action:** Wrap all raw `cv2.putText` text rendering over dynamic backgrounds with a local `draw_text_with_outline` helper function that draws a thicker black stroke (`thickness + 2`) behind the text using `cv2.LINE_AA`.
