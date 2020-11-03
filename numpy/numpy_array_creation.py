import numpy as np

print(np.zeros((3, 4),dtype=bool))     # crear una arreglo de 3x4 lleno de ceros

print(np.ones((3, 4),dtype=bool))      # crear un arreglo de 3x4 lleno de unos

mi_arreglo = np.identity(5).astype(int) # crear una matriz de identidad de 5x5
print(mi_arreglo)

tu_arreglo = np.ones_like(mi_arreglo)   # crear un arreglo igual a otro existente
print(tu_arreglo.shape)                 #shape muestra el tamaño del arreglo

x = np.arange(8)                        # crear un arreglo con 8 elementos
print(x)
print(x.reshape(2, 4))                  # cambiar el arreglo a 2x4 dimensiones