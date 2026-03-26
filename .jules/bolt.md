## 2024-06-25 - [Optimize Coordinate Math and Aggregations]
**Learning:** Native Python tuples and standard `math` functions (like `math.hypot`) are significantly faster for small-scale coordinate geometry in per-frame hot loops than instantiating and computing on NumPy arrays. Similarly, using native `sum() / len()` is faster than `np.mean()` for small lists, reducing instantiation and function call overhead.
**Action:** Replace `np.array` instantiation and `np.sqrt` with native tuples and `math.hypot`. Replace `np.mean` with native sum/len where list sizes are small in high-frequency loops.
