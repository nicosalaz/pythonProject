import numpy as np

x = np.arange(8)            # crear un arreglo con 0-7 elementos de una dimensión
print(x)
y = x.reshape(2, 4)         # creamos otro arreglo similar pero de 2x4 dimensiones
print(y)

print(max(x))

print(x.max())

print(x.argmax())

print(x.reshape(2, 4).argmax(1))

np.lookfor("solve")