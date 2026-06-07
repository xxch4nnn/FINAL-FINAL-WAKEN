## 2024-05-24 - NumPy Aggregation Overhead on Small Native Lists
**Learning:** In high-frequency Computer Vision loops, using NumPy aggregation functions like `np.mean` on very small native Python lists introduces substantial performance overhead (approx 30x faster with native math) due to type-checking and dispatch latency.
**Action:** Use standard Python math (`sum(list) / len(list)`) for small, fixed-size lists instead of NumPy in performance-critical paths.
