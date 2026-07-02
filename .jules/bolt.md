## 2024-07-02 - NumPy Distance Bottleneck
**Learning:** In high-frequency 2D vector distance calculations (like feature extraction per frame), `np.linalg.norm` and `np.sqrt` are significantly slower than native Python `math.hypot` or `math.dist` due to NumPy dispatch overhead on small arrays.
**Action:** Replace `np.linalg.norm` for 2D vectors and `np.mean`/`np.var` on small native lists with native `math` or standard arithmetic operations where possible, especially in tight loops.
