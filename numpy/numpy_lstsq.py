import numpy as np

# creamos el sistema de ecuaciones A * x = b
A = np.array([[1, 2, 1],
              [1,1,2],
              [2,1,1],
              [1,1,1]])
b = np.array([4,3,5,4])

# obtenemos el resultado del solver
x, residuals, rank, s = np.linalg.lstsq(A,b)
print(x)