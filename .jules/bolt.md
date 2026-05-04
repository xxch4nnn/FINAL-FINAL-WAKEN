## 2024-05-04 - [Optimize scalar distance calculations]
**Learning:** For scalar value mathematics, particularly Euclidean distances between 2D coordinates in pure Python contexts (like `int(x)**2 + int(y)**2`), `math.hypot(dx, dy)` significantly outperforms `np.sqrt` by over 90%. This is because it completely bypasses the C-API dispatch overhead of numpy, which becomes a major bottleneck when called multiple times per frame in a tight loop.
**Action:** Always prefer `math.hypot` over `np.sqrt` for pure Python scalar calculations unless vectorizing across large NumPy arrays simultaneously.
