## 2024-05-24 - Vectorize UI Geometry and Cache Intrinsics
**Learning:** Per-frame instantiation of NumPy arrays and Python-to-C++ context switching in hot loops (like `cv2.projectPoints` and `cv2.polylines`) cause significant CPU overhead. Vectorizing coordinate processing and caching constants (like camera intrinsics) improves performance.
**Action:** When drawing complex geometries (e.g., UI elements, 3D projections), compute static coordinates outside the render loop and batch OpenCV API calls to minimize context switches.
