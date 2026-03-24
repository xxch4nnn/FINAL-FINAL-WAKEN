## 2024-05-15 - Improve Text Legibility in OpenCV UI
**Learning:** Using `cv2.putText` directly over a live, dynamic camera feed often leads to poor legibility because text color and background contrast can be unpredictable.
**Action:** Always draw a slightly thicker black stroke (e.g., thickness=4) beneath the final text layer (e.g., thickness=2). This creates an outline effect ensuring text remains visible against any background.
