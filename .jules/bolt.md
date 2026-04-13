## 2024-05-18 - [Avoid NumPy Overheads in Hot Loops]
**Learning:** [Using NumPy functions (`np.array`, `np.sqrt`, `np.mean`) inside per-frame hot loops introduces unnecessary object creation and context-switching overheads that can degrade real-time performance. Python's native structures (tuples) and `math` module (e.g. `math.hypot`) are often faster for small-scale arithmetic operations common in CV coordinate geometry.]
**Action:** [Always prefer native Python tuples and the standard `math` library over NumPy for small, high-frequency per-point calculations in runtime processing loops.]
