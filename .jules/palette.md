## 2024-06-20 - OpenCV Text Outline Pattern
**Learning:** Raw OpenCV text (`cv2.putText`) lacks contrast and can be hard to read against dynamic video backgrounds, especially when standard colors blend with the scene.
**Action:** Created `draw_text_with_outline` local helper function and wrapped all `cv2.putText` calls for better readability over video feeds by drawing a thicker black border underneath the text using `cv2.LINE_AA`.
