## 2024-07-07 - Avoid NumPy for scalar and small list math
**Learning:** In high-frequency CV loops, using NumPy aggregation functions like `np.mean` on very small native Python lists, or `np.sqrt` for scalar math, introduces substantial dispatch and type-checking latency compared to standard Python operations.
**Action:** Use native Python math (`math.hypot` or `sum()/len()`) for small, fixed-size lists and scalar math to avoid NumPy overhead.
