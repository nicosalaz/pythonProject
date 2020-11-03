import numpy as np

# creamos el sistema de ecuaciones A * x = b
A = np.array([[1, 2, 1],
              [2, 4, 2], # Note que esta fila es la anterior multiplicada por 2
              [1, 0, 1]])
b = np.array([4,8,5])

# obtenemos el resultado del solver
x, residuals, rank, s = np.linalg.lstsq(A,b)
print(x)