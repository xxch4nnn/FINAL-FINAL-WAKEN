## 2024-05-24 - OpenCV UI Text Legibility and Accessibility
**Learning:** Text rendered with `cv2.putText` directly onto live camera feeds often suffers from poor legibility due to unpredictable background colors and lighting. Furthermore, missing keyboard hints in the UI reduces accessibility.
**Action:** Always use a 'text outline' technique (a thicker black stroke followed by a thinner white/colored fill) when rendering text on camera feeds, and explicitly render keyboard shortcuts on-screen to improve keyboard accessibility.
