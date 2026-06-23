## 2025-02-12 - Math over Numpy for Small Operations
**Learning:** In high-frequency loops (like per-frame cv2 processing), native Python math operations (`math.hypot`, `sum`/`len`) are significantly faster than NumPy equivalents (`np.sqrt`, `np.mean`) for small scalars or lists due to NumPy's type checking and dispatch latency.
**Action:** Always replace `np.sqrt` with `math.sqrt`/`math.hypot` and `np.mean` with `sum(list) / len(list)` for small fixed-size vectors/lists inside tight loops.
