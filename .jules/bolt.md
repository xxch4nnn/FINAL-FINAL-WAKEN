## 2024-05-24 - Math operations bottleneck
**Learning:** Using `np.sqrt` and `np.mean` for scalar values and small native Python lists in high-frequency CV loops adds measurable dispatch/type-checking latency.
**Action:** Always prefer native Python `math.hypot(x, y)` over `np.sqrt(x**2 + y**2)` and native `sum(list) / len(list)` over `np.mean(list)` for fixed-size small structures in performance-critical loops.
