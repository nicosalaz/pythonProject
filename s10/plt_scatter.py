import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.randn(N) # valores aleatorios en x
y = np.random.randn(N) # valores aleatorios en y


plt.scatter(x, y, color='red', marker='4') # graficamos los puntos x, y
plt.legend(['4'],loc = 'upper right')

plt.scatter(x, -y, color='blue', marker='*') # graficamos los puntos x, y

plt.grid()  # habilitamos una grilla
plt.show()
