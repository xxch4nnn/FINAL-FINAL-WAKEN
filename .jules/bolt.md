## 2025-04-19 - Optimize coordinate geometry in HandFeatureExtractor
**Learning:** Native Python `math.hypot` and `tuple` geometry calculations are significantly faster than instantiating `numpy` arrays for small, per-frame operations like those in `HandFeatureExtractor._get_euclidean` and `_to_pixel`. Same goes for simple aggregations (`sum(lst)/len(lst)` vs `np.mean`).
**Action:** Avoid `numpy` for localized coordinate operations inside high-frequency processing loops unless utilizing large vectorized arrays. Use native tuples and `math` module instead.
