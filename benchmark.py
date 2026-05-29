import timeit
import numpy as np
import math

def orig(p1, p2):
    dx = int(p1[0] - p2[0])
    dy = int(p1[1] - p2[1])
    return np.sqrt(dx**2 + dy**2)

def opt(p1, p2):
    dx = int(p1[0] - p2[0])
    dy = int(p1[1] - p2[1])
    return math.hypot(dx, dy)

print("np.sqrt:", timeit.timeit("orig([10, 20], [30, 40])", globals=globals(), number=1000000))
print("math.hypot:", timeit.timeit("opt([10, 20], [30, 40])", globals=globals(), number=1000000))
