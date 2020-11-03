# Inicializamos la lista
mi_lista = [1, 3, 6, 10]

# Se eleva a potencia de 2 cada termino
lista_ = [x ** 2 for x in mi_lista]

# Lo mismo usando un iterador
mi_iterador = (x ** 2 for x in mi_lista)

print(lista_)
print(mi_iterador)

print(next(mi_iterador))
print(next(mi_iterador))
next(mi_iterador)
print(next(mi_iterador))