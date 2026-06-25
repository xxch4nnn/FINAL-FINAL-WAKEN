## 2024-05-18 - Replacing NumPy Norms with Math in High-Frequency Loops
**Learning:** In high-frequency loops (e.g., frame-by-frame 2D vector distance calculations), using native Python `math.hypot(x, y)` or `math.dist(p, q)` is significantly faster than `np.linalg.norm` for scalars and small fixed-size lists due to NumPy's dispatch latency.
**Action:** Replace `np.linalg.norm` with `math.hypot` or `math.dist` in small vector magnitude and distance calculations in high-frequency computer vision code like `main_runtime.py`.
