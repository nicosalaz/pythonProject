lista1 = [1,3,4]
lista2 = lista1       # referencia
lista3 = list(lista1) # copia
lista3.append(6)
lista2.append(5)

# Que debe devolver cada lista ahora ?
print(lista1, lista2, lista3)