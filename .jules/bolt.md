## 2024-05-24 - NumPy Overhead in High-Frequency Loops
**Learning:** In high-frequency Computer Vision loops (like frame-by-frame feature extraction), using NumPy aggregation functions (`np.mean`, `np.sqrt`) on very small native Python lists or scalars introduces substantial performance overhead compared to standard Python operations (`sum()/len()`, `math.hypot`) due to type-checking and dispatch latency.
**Action:** Use native math operations (`sum()/len()`, `math.hypot`) for small, fixed-size lists and scalars to avoid NumPy overhead in hot paths.
