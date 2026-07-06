## 2024-07-06 - Native Math over NumPy for Scalar/Small Array Operations
**Learning:** In high-frequency loops (e.g., frame-by-frame 2D vector distance calculations), using native Python `math.hypot(x, y)` or `math.dist(p, q)` is significantly faster than `np.linalg.norm(array)`. NumPy aggregation functions introduce substantial dispatch latency on very small native Python lists/arrays.
**Action:** Always prefer `math.hypot` or `math.dist` for fixed-size small vectors inside tight loops, instead of NumPy operations.
