## 2024-06-14 - OpenCV Text Readability
**Learning:** Raw cv2.putText text rendering is often illegible against dynamic video backgrounds because the text can blend in with underlying pixels of the same color.
**Action:** Always wrap text rendering with a `draw_text_with_outline` helper function to add a black stroke behind the text, ensuring high contrast and accessibility.
