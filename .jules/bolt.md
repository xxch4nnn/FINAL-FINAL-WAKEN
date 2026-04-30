## 2024-05-01 - OpenCV Vectorization Pattern
**Learning:** In high-frequency computer vision loops (like 30+ FPS runtime scripts), calling `cv2.projectPoints` and `cv2.polylines` repeatedly in a loop (e.g. for each virtual piano key) causes significant Python-to-C++ context switching overhead.
**Action:** Always pre-compute static 3D geometry outside the main loop and use batched operations. Pass a flat array of points to `cv2.projectPoints`, then reshape the resulting 2D points to `(N, 4, 2)` and pass them directly to `cv2.polylines` to render all polygons in a single C++ call.
