## 2024-05-23 - math.hypot vs np.sqrt
**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)`. In pure Python scalar contexts, it bypasses NumPy's C-API dispatch overhead, providing an over 90% performance improvement.
**Action:** Use `math.hypot` instead of `np.sqrt` for distance calculations involving pure Python scalars.
