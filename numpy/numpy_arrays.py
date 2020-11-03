import numpy as np

# un arreglo unidimensional de tres posiciones implícitamente float
a = np.array([1.0,2.2,3.0])

# un arreglo bidimensional (matriz) NxN explicitamente entero
b = np.array([(1.5,2), (4,5.6)], dtype = int)

# un arreglo tridimensional de tipo complejo
c = np.array([(1.5,2,3.14), (4.56,0.99,6), (3,2.2,1)], dtype = complex)
print('a:',a, "\n\n",'b:', b, "\n\n",'c',c, "\n")

# es posible conocer el tipo de datos de los arreglos
print(a.dtype, b.dtype, c.dtype)

# se puede convertir el arreglo en otro tipo dado
print(a.astype(int))    