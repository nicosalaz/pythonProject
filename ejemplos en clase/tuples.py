t = 12345, 54321, 'Hola!'   # empaquetado de una tupla
print(t)
print(t[0])

# Las tuplas se pueden anidar
u = t, (1, 2, 3, 4, 5)
print (u)

# Las tuplas son immutables
#t[0] = 88888 # genera un error

# Las tuplas pueden contener objetos mutables como listas
v = ([1, 2, 3], [3, 2, 1])
print(v)

x, y ,z= t      # desempaquetado de una tupla
print(z,x,y)
