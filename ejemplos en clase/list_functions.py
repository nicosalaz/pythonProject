lista1 = [0, 1, 2]

# longitud de una lista
print(len(lista1)) # 3

# adicionar un elemento al final de la lista
lista1.append(5) # [0, 1, 2, 5]
print(lista1)

# eliminar un elemento de una lista
del lista1[1]# [0, 2, 5]
print('pop',lista1)

# insertar un elemento en una posición dada
lista1.insert(1, 42) # [0, 42, 2, 5]
print(lista1)

# ordenar la lista de menor a mayor
lista1.sort() # [0, 2, 5, 42]
print(lista1)

# reorganizar del final al inicio la lista
lista1.reverse() # [5, 2, 42, 0]
print(lista1)

lista1.extend([7,8]) #extiende la lista con los numeros ahí
print(lista1)

lista1.clear()

print(lista1)




