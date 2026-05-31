## 2024-05-31 - Scalar Math Optimization
**Learning:** In pure Python scalar contexts (especially after int casting), `math.hypot(dx, dy)` is significantly faster than `np.sqrt(dx**2 + dy**2)` by bypassing NumPy's C-API dispatch overhead. It safely returns a float instead of numpy.float64.
**Action:** Use `math.hypot` for 2D scalar Euclidean distance calculations instead of `np.sqrt` when dealing with individual points.
