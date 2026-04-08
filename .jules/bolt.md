## 2024-05-24 - OpenCV Vectorized Projection and Rendering
**Learning:** Calling `cv2.projectPoints` and `cv2.polylines` repeatedly inside a hot loop (like per-frame UI rendering) introduces significant Python-to-C++ context switching overhead. OpenCV functions natively support batch operations on arrays.
**Action:** When rendering multiple similar geometric shapes (like virtual keys), precompute the static 3D coordinate array, project all points in a single `cv2.projectPoints` call, and reshape the output to pass as a single batch to `cv2.polylines` instead of looping in Python.
