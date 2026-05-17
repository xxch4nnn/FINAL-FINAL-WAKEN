import numpy as np
import math
import time

def get_euclidean_np(p1, p2):
    dx = int(p1[0] - p2[0])
    dy = int(p1[1] - p2[1])
    return np.sqrt(dx**2 + dy**2)

def get_euclidean_math(p1, p2):
    dx = int(p1[0] - p2[0])
    dy = int(p1[1] - p2[1])
    return math.hypot(dx, dy)

p1 = [100, 200]
p2 = [150, 250]

t0 = time.time()
for _ in range(1000000):
    get_euclidean_np(p1, p2)
t1 = time.time()
print(f"NumPy: {t1-t0:.4f}s")

t0 = time.time()
for _ in range(1000000):
    get_euclidean_math(p1, p2)
t1 = time.time()
print(f"Math: {t1-t0:.4f}s")
