## 2024-06-18 - Replacing np.linalg.norm with math.hypot in high-frequency loops
**Learning:** In high-frequency operations like feature extraction in computer vision tracking scripts (e.g., Euclidean distance/magnitude for velocity and acceleration), using `np.linalg.norm` creates significant performance overhead due to NumPy's dispatch latency for 2D vectors.
**Action:** Replace `np.linalg.norm` calculations for explicit small (2D/3D) arrays with `math.hypot` for measurable speedup in continuous processing loops.
## 2024-06-18 - Replacing np.mean with native math for small lists
**Learning:** In high-frequency operations, using `np.mean` on small standard Python lists (e.g., history buffers) introduces substantial performance overhead due to NumPy array conversion and dispatch latency.
**Action:** Replace `np.mean(list)` with `sum(list) / len(list)` when computing the mean of small, fixed-size python lists within continuous processing loops.
