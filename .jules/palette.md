## 2024-06-03 - OpenCV Text Readability
**Learning:** Text rendered directly over dynamic camera feeds using `cv2.putText` can become unreadable when background colors match the text, causing severe accessibility and contrast issues.
**Action:** Always wrap `cv2.putText` calls in a local `draw_text_with_outline` helper function that first renders a thicker black background stroke (`thickness + 2`, using `cv2.LINE_AA`) before the foreground text to ensure strong contrast against any video background.
