## 2024-10-27 - OpenCV Text Contrast
**Learning:** Text rendered directly over dynamic video backgrounds via OpenCV (`cv2.putText`) often lacks sufficient contrast and becomes unreadable, negatively impacting accessibility and user experience.
**Action:** Always wrap `cv2.putText` calls with a `draw_text_with_outline` helper function that applies a thick black stroke behind the text using `cv2.LINE_AA` to ensure text legibility regardless of background variation.
