import time
import numpy as np

N, M = 100, 100
a = np.empty(10000).reshape(N, M)
b = np.random.rand(10000).reshape(N, M)
c = np.random.rand(10000).reshape(N, M)

t0 = time.time()

for i in range(N):
    for j in range(M):
        a[i, j] = b[i, j] + c[i, j]

print("Duración: %.4f s." % float(time.time() - t0))

t0 = time.time()

a = b + c

print("Duración: %.4f s." % float(time.time() - t0))
