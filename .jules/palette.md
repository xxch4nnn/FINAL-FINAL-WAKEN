## 2024-04-28 - OpenCV Text Contrast and Shortcut Discoverability
**Learning:** Text rendered directly over unpredictable live camera feeds using `cv2.putText` frequently lacks contrast, making UI elements unreadable. Furthermore, hidden keyboard shortcuts (like 'q' or 'ESC' to quit) reduce usability and accessibility.
**Action:** Use a "text outline" technique (drawing a thick black stroke followed by a thin white fill) for OpenCV text. Always explicitly render essential keyboard shortcuts on-screen (e.g., at the top of the frame) to improve interface discoverability.
