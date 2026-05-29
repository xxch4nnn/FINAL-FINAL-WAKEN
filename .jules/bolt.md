## 2025-02-28 - Optimize 2D Euclidean Distance

**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)`. In pure Python scalar contexts, it bypasses NumPy's C-API dispatch overhead, providing an over 90% performance improvement.

**Action:** Replace `np.sqrt(x**2 + y**2)` with `math.hypot(x, y)` for scalar math operations.
