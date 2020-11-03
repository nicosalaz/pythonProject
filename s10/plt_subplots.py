import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x ** 2)

x = np.linspace(-1, 5, num=30)

fig, axes = plt.subplots(1, 2, sharey=True)

axes[0].plot(x, f(x), color="blue")
axes[0].set_xlabel("Eje x")
axes[0].grid(True)

axes[1].plot(x, -f(x), 'r')
axes[1].set_xlabel("Eje x de la gráfica derecha")
axes[1].grid(True)

plt.show()