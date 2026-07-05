## 2024-05-24 - Avoid np.linalg.norm in high-frequency loops
**Learning:** Using `np.linalg.norm()`, `np.mean()`, and `np.var()` for 2D vectors or small arrays in a tight frame-by-frame loop introduces significant NumPy dispatch latency compared to native Python math operations.
**Action:** Replace `np.linalg.norm()` with `math.dist()` for point-to-point distances, `math.hypot()` for vector magnitudes, and use list comprehensions with `sum()` for small array aggregations to improve feature extraction latency.
