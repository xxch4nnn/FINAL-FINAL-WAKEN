## 2024-05-30 - Native Python Math vs NumPy in High-Frequency Loops
**Learning:** In high-frequency calculations (e.g., Euclidean distance in feature extraction loop), native Python `math` operations are significantly faster than `np.linalg.norm` for computing distances on small vectors due to NumPy's dispatch latency. The same applies for small array aggregation functions like `np.mean` and `np.var`.
**Action:** Replace `np.linalg.norm`, `np.mean`, and `np.var` with native `math` operations (`math.hypot`, `math.dist`) and list comprehensions for small native collections in tight loops.
