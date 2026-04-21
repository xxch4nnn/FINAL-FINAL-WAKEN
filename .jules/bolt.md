## 2024-04-21 - Vectorize OpenCV Projections
**Learning:** Calling OpenCV functions like `cv2.projectPoints` and object instantiations like `np.array` in a per-frame hot loop creates significant Python-to-C++ context switching and memory allocation overhead. OpenCV batch drawing functions natively support multi-dimensional batched processing.
**Action:** Always precompute static 3D geometry outside hot loops. Reshape batched point arrays to pass directly into `cv2.projectPoints` and `cv2.polylines` to minimize API calls and memory reallocation.
