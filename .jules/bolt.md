## 2024-05-18 - Optimize Math Operations
**Learning:** In high-frequency loops (e.g. `main_runtime.py`'s feature extractor running 30 times a second), using NumPy aggregations like `np.linalg.norm`, `np.mean`, and `np.var` on small arrays or single coordinate pairs introduces significant dispatch and overhead latency. Native Python math functions (`math.hypot`, `math.dist`, and `sum`) are noticeably faster for small fixed-size vectors.
**Action:** Replace 1D/2D numpy math calls with `math.hypot`, `math.dist`, and list comprehensions using native math in hot paths.
