## 2024-05-24 - Performance Optimization: math.hypot vs np.sqrt
**Learning:** `math.hypot(dx, dy)` is over 15x faster than `np.sqrt(dx**2 + dy**2)` for 2D Euclidean distance calculations with pure Python scalars (e.g., after integer casting).
**Action:** Replace `np.sqrt` with `math.hypot` in pure Python scalar operations to improve performance without side effects.
