## 2025-02-14 - NumPy Overhead in High-Frequency Loops
**Learning:** In high-frequency CV operations on small data structures (like scalars or small native lists in frame-by-frame processing), native Python `math.hypot` and `sum()/len()` significantly outperform NumPy equivalents (`np.sqrt`, `np.mean`) due to NumPy's dispatch and type-checking latency.
**Action:** Always prefer native Python `math` operations and aggregations for scalars and small, fixed-size lists inside tight computer vision loops to reduce overhead.
