import numpy as np

# creamos el arreglo de 6x6 con step de 1 en las columnas y
# step de 10 en las filas
filas = np.arange(6)
#print(filas)
columnas = np.arange(0, 51, 10) [:, np.newaxis]
#print(columnas)

a = filas + columnas
print(a)
# lo anterior es equivalente a:
#   a = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]

# accediendo a los elementos de la matriz
# print (a[0, 3:5])
# print (a[4:, 4:])
# print (a[:, 2])
#si hacemos un slicing [desde:hasta:de cuanto en cuento] EJ:(parecido al range del for)
#       fila  columna
#print(a[2:5:2,0:5:2])
mask = np.array([0,1,1,0],dtype=bool).reshape(2,2)
b = a[0::5,0::5]
print('solucion:',b[mask])