import numpy as np

# creamos el sistema de ecuaciones A * x = b
A = np.array([[1, 2, 1],
              [0, 1, 1],
              [1, 0, 1]])
b = np.array([4, 3, 5])

# obtenemos el resultado del solver
x = np.linalg.solve(A, b)
print(x)