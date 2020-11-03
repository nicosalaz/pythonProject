import numpy as np

# creamos el arreglo de 6x6 con step de 1 en las columnas y
# step de 10 en las filas
a = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]

# imprimimos indicando con enteros los indices del arreglo
print (a[(range(0,5), range(1,6))])
print (a[3:, [0,2,5]])

# creamos una máscara de valores booleanos
mask = np.array([1,0,1,0,0,1], dtype=bool)
print(mask)
#imprimimos solo los elementos donde la mascara es True
print(a[mask,2])

# i = np.array([1,2,3])
# j = np.array([4,5])

#print(i+j)