import timeit
import math
import numpy as np

setup = "import math; import numpy as np; dx = 10; dy = 20"
stmt1 = "np.sqrt(dx**2 + dy**2)"
stmt2 = "math.hypot(dx, dy)"

t1 = timeit.timeit(stmt1, setup=setup, number=1000000)
t2 = timeit.timeit(stmt2, setup=setup, number=1000000)

print(f"np.sqrt: {t1:.4f} seconds")
print(f"math.hypot: {t2:.4f} seconds")
print(f"Improvement: {(t1-t2)/t1*100:.2f}%")
