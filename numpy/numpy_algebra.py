import numpy as np

# Definimos la matriz A
A = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 5)
print('A:',A)

# Obtenemos la matriz transpuesta de A
print ('A.T:',A.T)

# Obtenemos la norma de A
print('Norma:',np.linalg.norm(A))

# Obtenemos el determinante de un slice de A de 2x2
print('determinante:',np.linalg.det(A[1:2,1:2]))

# Confirmamos que el determinante de su transpuesta es el mismo
print(np.linalg.det(A[1:2,1:2]).T)