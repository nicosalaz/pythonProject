import numpy as np

X = np.ones(10)
Y = np.ones(10)

# realizamos el cálculo utilizando el operador +
Z = 2*X + 2*Y   # Dos arreglos intermedios son creados (2*X, 2*Y)
print(Z)

# inicializamos nuevos arreglos con copias y zeros
X1 = X.copy()
Y1 = Y.copy()
Z1 = np.zeros(10)

# realizamos el cálculo utilizando la función multiply y add
np.multiply(X1, 2, out=X)
np.multiply(Y1, 2, out=Y)
np.add(X, Y, out = Z1) # Ningún arreglo intermedio es creado
print(Z1)