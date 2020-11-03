import numpy as np

# Genera 5 números aleatorios a partir de una distribución uniforme [0, 1)
print(np.random.rand(5))

# Crea una matriz entera aleatoria de 5x5 que varía de 10 (inclusive) a 20 (inclusive)
print(np.random.randint(10, 20, (5, 5)))

# Genera 5 números aleatorios a partir de una distribución normal estándar
# (media = 0, desviación estándar = 1)
print(np.random.randn(5))

# Este resultado también se puede lograr con el np.random.normal más general
print(np.random.normal(0, 1, 5))

# se puede definir la semilla
np.random.seed(0)
print(np.random.randn(5))

# Seleccione tres letras al azar con reemplazo (el mismo elemento se puede elegir varias veces) y sin reemplazo
letras = list('abcde')
print(np.random.choice(letras, 3))
print(np.random.choice(letras, 3,replace=False))
