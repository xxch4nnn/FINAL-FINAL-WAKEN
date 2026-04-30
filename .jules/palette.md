## 2024-05-24 - High-Contrast UI Text Overlay

**Learning:** When overlaying text on unpredictably changing live camera feeds, simple colored text (like `cv2.putText` with just one color) often becomes unreadable depending on the background brightness or complexity. This is a significant accessibility and usability issue for applications that rely on immediate visual feedback.

**Action:** Always implement a "text outline" technique for UI text over live feeds. Draw the text first with a thick black stroke, then draw the same text directly over it with a thinner, lighter color (e.g., white or bright green). This ensures the text maintains high contrast and remains legible regardless of the background. Furthermore, explicit on-screen keyboard hints should be placed in consistent, high-visibility areas like the top of the frame.
