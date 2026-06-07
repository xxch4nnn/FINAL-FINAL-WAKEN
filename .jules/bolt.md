## 2026-06-06 - NumPy Overhead on Small Python Lists
**Learning:** Using `np.mean` on short native Python lists (like the 10-element history buffer in feature extraction) creates substantial overhead (~45-50% slower) compared to built-in `sum(list) / len(list)` operations due to NumPy's type checking, dispatching mechanisms, and array conversions.
**Action:** For small, fixed-size python lists in high-frequency loops (like per-frame CV processing), always prefer native Python math built-ins (`sum`, `/`, `min`, `max`) over NumPy functions.
