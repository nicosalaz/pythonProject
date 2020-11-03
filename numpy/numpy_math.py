import numpy as np

a = np.array([1,2,3])   # creamos los arreglos a operar
b = np.array([(1,2,3), (4,5,6)], dtype = float)
print("Arreglo a: ", a, "\ny arreglo b:\n", b)

print("Suma a+b:\n", a+b) # suma de matrices

print("Resta a-b:\n", a-b) # resta de matrices

print("División a/b:\n", a/b) # división de matrices

print("Multiplicación a*b:\n", a*b) # multiplicación de matrices

print("Exponeciación de a:\n", np.exp(a)) # exponentes de todos los elementos

print("Raíz cuadrada de b:\n", np.sqrt(b)) # raiz cuadrada de todos los elementos

print("Seno de a:\n", np.sin(a))  # función seno de todos los elementos

print("Coseno de b:\n", np.cos(b))  # función coseno de todos los elementos

print("Logaritmo de a:\n", np.log(a))  # logaritmo de todos los elementos

middle_dot = '\u00B7'
print("Producto punto b"+middle_dot+"a:\n", b.dot(a))  # producto punto b . a


