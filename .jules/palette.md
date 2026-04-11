## 2024-04-11 - Text Outline for Video Feeds
**Learning:** Standard text overlay (`cv2.putText`) often becomes unreadable against live camera feeds due to varying background colors and lighting. Discoverability of keyboard shortcuts is also often poor when not explicitly drawn on screen.
**Action:** Implemented `draw_text_with_outline` to add a black stroke around text elements, significantly improving legibility across diverse backgrounds, and explicitly added keyboard shortcut hints at the top of the frame.
