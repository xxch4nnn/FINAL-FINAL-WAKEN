## 2024-05-15 - Hot Loop NumPy Overhead
**Learning:** For small array creations (e.g., length 2 coordinate pairs) and basic arithmetic like Euclidean distance or mean calculations inside per-frame hot loops, instantiating NumPy arrays and using NumPy functions (like np.sqrt, np.mean) introduces significant overhead compared to native Python tuples and math module functions (math.hypot, sum()/len()).
**Action:** Replace small NumPy structures and methods in high-frequency computer vision loops with native Python equivalents to eliminate instantiation and C++ context-switching bottlenecks.
