lista1 = [] # creación de una vista vacía manualmente
print(lista1)

lista1 = [1, 2.0, 'mundo' ] # creación de una lista con valores de diferentes tipos
print(lista1)

lista1[0] = 'hola' # manipulación de elementos de la lista
del lista1[1]
print(lista1)

lista1[0] = list(lista1) # creación de sublistas
print(lista1)

print("La longitud de la lista es: ",len(lista1)) # longitud de la cadena

print(lista1[1][-2]) #toma la ubicacion en lista y la posicion de lo que haya allí



# Asignación solo en elementos con índice presente en la lista
#lista1[2] = 'Esto genera un error de out-of-range'