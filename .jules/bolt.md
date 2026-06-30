## 2025-05-18 - NumPy Dispatch Latency in Real-time Feature Extraction
**Learning:** Using NumPy aggregations (`np.mean`, `np.var`) and math (`np.linalg.norm`) on very small native Python arrays introduces substantial dispatch latency which compounds in high-frequency computer vision loops (e.g., 30 FPS feature extraction).
**Action:** Always replace `np.linalg.norm` and `np.sqrt` with `math.hypot` and `math.dist` for fixed-size small vectors, and use native math operations like `sum()` for small lists to avoid type-checking and dispatch latency.
