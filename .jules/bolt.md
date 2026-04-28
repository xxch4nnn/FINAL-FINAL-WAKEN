## 2024-05-18 - Vectorize OpenCV Loops
**Learning:** In high-frequency CV loops (`while running:`), calling `cv2.projectPoints` and `cv2.polylines` repeatedly in a Python `for` loop causes severe Python-to-C++ context switching overhead. The arrays can be pre-computed before the loop and batched.
**Action:** Always pre-calculate static 3D coordinates and vectorize projections into a single batched NumPy array, using `cv2.polylines(vis_frame, pts_2d_reshaped, ...)` for rendering multiple items in one API call.
