## 2025-02-28 - Euclidean Distance Optimization
**Learning:** Pure Python `math.hypot` is over 90% faster than `np.sqrt(dx**2 + dy**2)` for pure Python scalar variables, largely bypassing numpy's C-API dispatch overhead for scalar coordinates that have been cast to integers.
**Action:** In `src/features/extractor.py`, replace `np.sqrt` with `math.hypot` inside `_get_euclidean` when calculating Euclidean distance between pixel coordinates. Ensure `math` module is imported.
