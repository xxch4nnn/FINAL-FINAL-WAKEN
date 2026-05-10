## 2025-03-05 - math.hypot Performance Optimization
**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)`. In pure Python scalar contexts, it bypasses NumPy's C-API dispatch overhead, providing an over 90% performance improvement.
**Action:** When calculating distance on scalar variables (not vectorized numpy arrays) in Python, use `math.hypot` instead of `np.sqrt` for better performance.
