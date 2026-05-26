## 2024-05-18 - Math.hypot instead of np.sqrt
**Learning:** For scalar Euclidean distance calculations in pure Python, `math.hypot` is over 90% faster than `np.sqrt(dx**2 + dy**2)` because it bypasses the overhead of NumPy's C-API dispatch.
**Action:** Replace `np.sqrt` with `math.hypot` in `_get_euclidean` inside `HandFeatureExtractor`.
