## 2024-05-14 - High-Contrast Text Outline and Keyboard Hints
**Learning:** Text rendered directly over unpredictable live video feeds (like a camera) suffers from poor contrast, making it inaccessible. Additionally, hidden keyboard shortcuts (like pressing 'q' to quit) reduce the usability of OpenCV GUI applications.
**Action:** Implemented a reusable `draw_text_with_outline` pattern in Python/OpenCV to draw a thick black stroke followed by a thin white fill for improved legibility. Also, explicitly rendered an on-screen keyboard hints HUD at the top of the frame for better discoverability.
