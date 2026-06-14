## 2024-05-18 - math.hypot vs np.sqrt
**Learning:** In high-frequency loops (e.g., frame-by-frame 2D vector distance calculations), using native Python `math.hypot(x, y)` is significantly faster than `np.sqrt(x**2 + y**2)` or `np.linalg.norm(array)`. NumPy functions carry a dispatch overhead that drastically slows down scalar math in tight loops.
**Action:** Always prefer `math` module functions like `math.hypot` over `numpy` when computing scalar values inside tight, fixed-size mathematical operations.
