## 2024-05-15 - [Vectorized OpenCV Operations]
**Learning:** Calling `cv2.projectPoints` and `cv2.polylines` repeatedly inside a hot loop for rendering static UI elements (like piano keys) creates significant Python-to-C++ context switching overhead, making the loop slower.
**Action:** When rendering multiple similar geometric shapes, precompute their 3D coordinates into a single batched numpy array and use a single vectorized API call to render them simultaneously.
