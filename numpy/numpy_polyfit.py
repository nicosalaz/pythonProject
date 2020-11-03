import numpy as np

npoints = 20
slope = 2
offset = 3
x = np.arange(npoints)
y = slope * x + offset + np.random.normal(size=npoints)
p = np.polyfit(x,y,1)           # El último argumento es el grado del polinomio

import matplotlib.pyplot as plt

f = np.poly1d(p)                # Llamamos a f(x)

print(p)

plt.plot(x, y, 'ro', label="Data")
plt.plot(x,f(x), 'g-',label="Polyfit")
plt.legend()
plt.show()