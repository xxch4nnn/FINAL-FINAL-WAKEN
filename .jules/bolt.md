## 2024-05-24 - [Optimize Extractor Hot Loop]
**Learning:** Instantiating small `np.array` objects and calling `np` functions like `np.sqrt` or `np.mean` for simple calculations inside a per-frame hot loop introduces significant overhead compared to native Python operations.
**Action:** Use native Python tuples, `math.hypot`, and `sum() / len()` for small, frequent calculations (like in the computer vision hot loops) instead of Numpy to reduce instantiation and function call overhead.
