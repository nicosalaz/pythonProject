import numpy as np
#
x = np.zeros(9) # vistas de un arreglo
print(x)

x_view = x[3:]
print(x_view)

x_view[...] = 1
print(x)

x_copy = x[[6,7,8]] # copias de un arreglo con indexado fancy
print(x_copy)

x_copy[...] = 1
print(x)

print(x_view.base is x) # preguntamos si es vista o copia
print(x_copy.base is x)
print(np.may_share_memory(x_view, x)) # o podemos preguntar
print(np.may_share_memory(x_copy, x)) # si comparten memoria