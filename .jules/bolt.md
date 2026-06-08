## 2026-06-08 - Small List Aggregation Bottleneck
**Learning:** In high-frequency CV loops like `process_live` inside `HandFeatureExtractor`, using `np.mean()` on very small lists (e.g., 2-10 items) is substantially slower than native Python math (`sum(list) / len(list)`) due to numpy's type-checking and array conversion overhead.
**Action:** Replace `np.mean()` with native math for small, fixed-size historical buffer aggregations.
