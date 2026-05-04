## 2024-05-24 - Performance comparison of math.hypot vs np.sqrt
**Learning:** For 2D Euclidean distance calculations between scalar coordinates (especially after integer casting), `math.hypot(dx, dy)` is significantly more efficient than `np.sqrt(dx**2 + dy**2)` in pure Python scalar context, yielding an over 90% improvement (from 1.85s to 0.16s for 1M iterations).
**Action:** Use `math.hypot` instead of `np.sqrt` for point-to-point distance calculations involving individual coordinate pairs rather than large vectorized arrays.
