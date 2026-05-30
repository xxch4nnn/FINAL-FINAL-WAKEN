## 2024-05-18 - Math Hypot vs Numpy Sqrt Performance
**Learning:** For scalar Euclidean distance calculations `np.sqrt(dx**2 + dy**2)` is substantially slower than `math.hypot(dx, dy)`. Since we're parsing integer pixel values for the MediaPipe feature extraction rather than calculating bulk array operations, the pure Python overhead of dispatching to NumPy's C-API is a massive bottleneck.
**Action:** Use `math.hypot` instead of `np.sqrt` for Euclidean distances on scalar numbers in python to see a ~90% performance boost.
