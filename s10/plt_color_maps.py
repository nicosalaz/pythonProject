import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.randn(N) # valores aleatorios en x
y = np.random.randn(N) # valores aleatorios en y

s = 50 + 50 * np.random.randn(N) # tamaño de los puntos
c = np.random.randn(N) # colores de los puntos

plt.scatter(x, y, s=s, c=c, cmap=plt.cm.Blues)
plt.colorbar()

plt.scatter(x, -y, s=s, c=c, cmap=plt.cm.Oranges)
plt.colorbar()
plt.grid()
plt.show()