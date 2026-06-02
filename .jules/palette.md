# Palette's Journal

## UX Learnings
## 2024-05-18 - Text Contrast in OpenCV
**Learning:** Raw OpenCV text rendering lacks built-in contrast support, making dynamic overlays completely unreadable when the camera background color matches the text color (e.g., white text on a bright background).
**Action:** Always implement a `draw_text_with_outline` local helper function to render a thicker black background stroke behind the primary text for accessibility and readability across any video feed.
