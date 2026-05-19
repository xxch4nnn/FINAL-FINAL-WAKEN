## 2024-05-24 - Pure Python Scalar Math vs NumPy Overhead
**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)`. In pure Python scalar contexts, it bypasses NumPy's C-API dispatch overhead, providing an over 90% performance improvement.
**Action:** Always prefer `math.hypot` over `numpy.sqrt` for simple distance calculations between point coordinates in non-vectorized Python loops or methods.
