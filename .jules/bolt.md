## 2024-06-02 - math.hypot vs np.sqrt
**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)`. In pure Python scalar contexts, it bypasses NumPy's C-API dispatch overhead, providing an over 90% performance improvement.
**Action:** Use `math.hypot(dx, dy)` instead of `np.sqrt(dx**2 + dy**2)` for scalar 2D distance calculations to maximize performance without breaking downstream logic.
