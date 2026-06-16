## 2024-05-26 - OpenCV Text Outline Pattern
**Learning:** Raw OpenCV text rendering (`cv2.putText`) often lacks sufficient contrast and blends into dynamic video backgrounds, causing significant accessibility and readability issues for users.
**Action:** All raw `cv2.putText` calls over dynamic video backgrounds must be wrapped with a local `draw_text_with_outline` helper function that first draws a thicker black stroke (`color=(0, 0, 0)`, `thickness + 2`, `cv2.LINE_AA`) behind the primary text to ensure contrast.
