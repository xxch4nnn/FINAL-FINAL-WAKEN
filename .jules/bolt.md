## 2024-05-24 - Math vs Numpy for Scalars
**Learning:** Using `np.sqrt` for calculating distance with small python scalar integers is significantly slower (~10x) than using `math.hypot`. This is because numpy is optimized for large vectorized arrays and suffers from overhead when used on singular elements.
**Action:** Always use `math.hypot` for scalar Euclidean distance calculations in Python.
