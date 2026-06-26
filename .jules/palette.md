## YYYY-MM-DD - OpenCV Text Readability Pattern
**Learning:** In dynamic video backgrounds, raw OpenCV text without outlines is often unreadable against light or complex visual inputs.
**Action:** Always wrap `cv2.putText` with a helper function `draw_text_with_outline` that renders a thicker black background stroke behind the primary text.
