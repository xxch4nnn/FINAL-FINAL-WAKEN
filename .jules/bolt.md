## 2024-05-24 - High-Frequency Loop Aggregation Overheads
**Learning:** In high-frequency Computer Vision loops (e.g., frame-by-frame feature extraction), using NumPy aggregation functions like `np.mean` on very small native Python lists introduces substantial performance overhead compared to standard Python operations like `sum(list) / len(list)`.
**Action:** Use native math for small, fixed-size lists to avoid type-checking and dispatch latency.
