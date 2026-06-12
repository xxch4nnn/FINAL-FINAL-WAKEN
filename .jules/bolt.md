## 2024-05-18 - Fast Math Operations in High Frequency Loops
**Learning:** In high-frequency operations like feature extraction in the camera loop, using `np.sqrt` for scalars and `np.mean` for small Python lists is a bottleneck because of NumPy's overhead. Using native Python `math.sqrt` and `sum(list) / len(list)` leads to a ~50% reduction in execution time for `process_live`.
**Action:** Replace `np.sqrt` with `math.sqrt` and `np.mean` with native math (`sum(x)/len(x)`) in `src/features/extractor.py`.
