## 2024-05-24 - [Instantiation Overhead in Hot Loops]
**Learning:** Precomputing static NumPy arrays like camera intrinsics (K, D) inside per-frame loops (e.g., in OpenCV applications) causes significant instantiation overhead and garbage collection pressure, negatively impacting FPS.
**Action:** Always precompute static matrices and dimensions outside of hot per-frame loops unless they dynamically change.
