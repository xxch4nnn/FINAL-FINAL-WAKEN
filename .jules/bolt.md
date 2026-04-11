## 2024-05-24 - Avoid NumPy Overhead in Hot Loops
**Learning:** Using native Python tuples and math functions like `math.hypot` is faster than instantiating NumPy arrays (`np.array`) and calling NumPy functions (`np.sqrt`, `np.mean`) inside high-frequency per-frame loops.
**Action:** Prioritize standard Python data structures and math functions for simple calculations in hot loops to reduce context switching and object creation overhead.
