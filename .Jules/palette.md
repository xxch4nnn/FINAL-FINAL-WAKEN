## 2024-05-20 - High Contrast Text for Dynamic Camera Feeds
**Learning:** Raw `cv2.putText` fails WCAG contrast guidelines against unpredictable real-world camera feeds (variable lighting, skin tones, etc.), making critical UI elements and shortcuts illegible.
**Action:** Always render a contrasting outline (e.g., black border behind colored text) using a custom `draw_text_with_outline` function to ensure persistent text readability across all background conditions. Persistent shortcuts must also avoid overlapping with dynamic status text.
