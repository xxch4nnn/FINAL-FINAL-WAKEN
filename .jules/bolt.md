## 2026-06-26 - Native Math vs NumPy in High-Frequency Loops
**Learning:** In high-frequency CV loops like frame-by-frame feature extraction, NumPy's overhead for tiny arrays (e.g. `np.linalg.norm` and `np.mean`) makes it significantly slower than native Python's `math.hypot`, `math.dist` and simple list comprehensions/aggregations.
**Action:** Always prefer `math` over `numpy` for small, fixed-size vectors in tight execution loops.
