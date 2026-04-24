## 2024-05-24 - OpenCV Batch Drawing Optimization
**Learning:** `cv2.projectPoints` and `cv2.polylines` have significant Python-to-C++ context switching overhead when called in a loop for multiple shapes. Static 3D coordinates (like virtual keys relative to an ArUco marker) should be precomputed outside hot loops.
**Action:** When drawing multiple shapes (like virtual keys), pre-compute the 3D geometry into a single array. Use one vectorized `cv2.projectPoints` call, then reshape the output to `(N, 4, 2)` and pass it as a batch directly to `cv2.polylines` rather than iterating.
