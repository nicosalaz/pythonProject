import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# creación del histograma
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g')

plt.xlabel('Inteligentes')
plt.ylabel('Probabilidad')
plt.title('Histograma de IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()