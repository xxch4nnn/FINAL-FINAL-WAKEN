## 2024-05-15 - Optimizing Feature Extraction Math
**Learning:** In high-frequency computer vision loops (e.g. Euclidean distance in feature extraction), native Python `math.hypot` and `math.sqrt` are significantly faster than `np.sqrt` for scalars. Using `np.mean` on very small native Python lists introduces substantial performance overhead compared to standard Python operations like `sum(list) / len(list)`.
**Action:** Always replace these NumPy operations with native Python math for fixed-size small lists/vectors inside tight loops to avoid NumPy's dispatch latency.
