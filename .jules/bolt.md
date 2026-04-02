## 2024-04-02 - Hot Loop Math Optimization
**Learning:** Numpy operations (like `np.mean` or `np.sqrt`) and array instantiations in per-frame high-frequency loops (like hand feature extraction) cause significant overhead compared to native Python operations, especially for small data structures like points or small lists.
**Action:** Replace `np.array` instantiations with native Python `tuples`, `np.sqrt` with `math.hypot`, and `np.mean` with `sum() / len()` in critical paths where data sizes are small to maximize performance and avoid unnecessary overhead.
