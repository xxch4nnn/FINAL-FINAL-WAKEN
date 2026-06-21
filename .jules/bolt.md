## 2024-05-14 - Replace np.linalg.norm with math.hypot in high-frequency loops
**Learning:** In high-frequency operations like feature extraction per frame, `np.linalg.norm` is significantly slower (by ~10x) than native python `math.hypot` when calculating vector distances for scalar and 1D arrays (x, y coords). This applies strictly when extracting features for machine learning pipelines in this project, particularly in `LiveFeatureExtractor`.
**Action:** Replace `np.linalg.norm` operations on explicit (x, y) coordinates with `math.hypot` for speed.
