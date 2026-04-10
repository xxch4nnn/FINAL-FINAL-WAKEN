## 2024-04-10 - [Batch Drawing Optimization]
**Learning:** In high-frequency CV loops (like per-frame OpenCV rendering), iterating to project points (`cv2.projectPoints`) and draw shapes (`cv2.polylines`) causes massive Python-to-C++ context switching overhead.
**Action:** Always pre-compute static geometry arrays outside the main loop and use a single vectorized API call for batch projection and batch drawing (e.g., reshaping points into a batched array for `cv2.polylines`).
