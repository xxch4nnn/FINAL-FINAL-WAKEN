## 2026-03-29 - [NumPy Overhead in Hot Loops]
**Learning:** Using heavy NumPy functions (`np.array`, `np.sqrt`, `np.mean`) for simple scalar and tiny list operations in a hot loop (like real-time per-frame feature extraction) introduces significant instantiation and operational overhead.
**Action:** Replace NumPy array creation with native Python `tuples`, `np.sqrt` with `math.hypot`, and `np.mean` with native aggregations like `sum() / len()` to achieve multi-fold speedups in high-frequency calculations without sacrificing readability.
