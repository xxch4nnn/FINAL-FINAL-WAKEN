## 2024-03-24 - Performance: Avoid np.linalg.norm for small 2D/3D vectors
**Learning:** Using `np.linalg.norm` for small native arrays (2 elements) inside high-frequency loops (e.g. frame-by-frame 2D vector distance calculations) is significantly slower than using native Python `math.hypot` or `math.dist` due to numpy's overhead and dispatch latency.
**Action:** Replace `np.linalg.norm` with `math.hypot(x, y)` or `math.dist(p1, p2)` for fixed-size small vectors to avoid numpy's dispatch latency. `math.dist` safely accepts 1D NumPy arrays.
