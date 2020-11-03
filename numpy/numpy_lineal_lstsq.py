import numpy as np

npoints = 20
slope = 2
offset = 3
x = np.arange(npoints)
y = slope * x + offset + np.random.normal(size=npoints)

import matplotlib.pyplot as plt

A = np.vstack([x,np.ones(npoints)]).T
m, c = np.linalg.lstsq(A, y)[0]

plt.plot(x, y, 'bo', label="Data")
plt.plot(x, m*x+c, 'g--',label="Least Squares")
plt.show()