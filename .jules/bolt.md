## 2024-05-14 - Use native math instead of numpy for small lists in loops
**Learning:** In high-frequency Computer Vision loops (e.g., frame-by-frame feature extraction), using NumPy aggregation functions like `np.mean` on very small native Python lists introduces substantial performance overhead compared to standard Python operations like `sum(list) / len(list)`.
**Action:** Use native math for small, fixed-size lists to avoid type-checking and dispatch latency.
## 2024-05-14 - Prefer math.sqrt over np.sqrt for scalars
**Learning:** In high-frequency calculations (e.g., Euclidean distance in feature extraction), native Python `math.sqrt` is significantly faster than `np.sqrt` when computing scalars.
**Action:** Always prefer `math` over `numpy` for scalar math operations inside tight loops.
