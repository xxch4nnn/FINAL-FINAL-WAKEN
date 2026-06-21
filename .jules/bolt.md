## 2025-05-18 - Fast Euclidean Math
**Learning:** In high-frequency tight loops like the frame-by-frame feature extraction, native `math.hypot` and `sum(list) / len(list)` are significantly faster (up to ~5x) than `np.linalg.norm` and `np.mean` for small fixed-size vectors due to avoiding NumPy dispatch latency.
**Action:** Replace `np.linalg.norm` and `np.mean` with native math operations for small vectors when possible.
