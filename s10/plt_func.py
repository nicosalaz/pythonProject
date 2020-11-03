import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x ** 2)

x = np.linspace(-1, 5, num=30) # dominio de la función

plt.plot(x, f(x), label="Función f(x)")
plt.xlabel("Eje $x$")
plt.ylabel("$f(x)$")
plt.legend()
plt.title("Función $f(x)$")
plt.grid(linestyle="--", color="red")
plt.show()