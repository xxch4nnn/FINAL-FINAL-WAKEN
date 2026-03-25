## 2024-05-24 - Python Hot Loop Optimization
**Learning:** Using numpy arrays and `np.mean()` in small lists during a hot loop (like per-frame CV processing) adds significant instantiation and conversion overhead compared to native python types and math functions.
**Action:** Always prefer native python tuples and math module functions (like `math.hypot`) or native python functions (`sum() / len()`) over `numpy` when working with small, per-frame data lists to increase performance.
