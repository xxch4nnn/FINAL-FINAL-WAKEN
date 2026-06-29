## 2024-05-24 - High-Frequency Loop Overhead with NumPy Aggregations
**Learning:** In high-frequency loops like `HandFeatureExtractor.process_live()`, computing small rolling averages over lists (e.g., `np.mean` over a 10-item deque) using NumPy introduces substantial type-checking and dispatch latency compared to native Python math operations like `sum(list) / len(list)`.
**Action:** Replace `np.mean(disps)` and `np.mean(raw_size_changes)` with native python `sum(disps) / len(disps)` when the list size is small (buffer_size=10), to avoid unnecessary performance overhead.
