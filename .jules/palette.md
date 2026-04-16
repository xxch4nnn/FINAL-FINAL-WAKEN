## 2024-04-16 - OpenCV Text Contrast and Discoverability
**Learning:** Live camera feeds have unpredictable backgrounds, causing standard `cv2.putText` text to become unreadable. Additionally, essential keyboard shortcuts (like quitting) are often hidden in the code, leading to poor UX and discoverability.
**Action:** Always implement a 'text outline' technique (draw a thick black stroke, followed by a thin white fill) for on-screen text in OpenCV. Also, explicitly render essential keyboard shortcuts on the UI to guide the user.
