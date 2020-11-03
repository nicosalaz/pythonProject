# usando un ciclo para convertir cada item de la lista
amigos = ['alfredo', 'juana', 'william', 'freddy']
amigos_mayusculas = []

for amigo in amigos:
    amigo_ = amigo.upper()
    amigos_mayusculas.append(amigo_)

print(amigos_mayusculas)

# usando la función map
amigos_mayusculas_map = list(map(str.upper, amigos))

print(amigos_mayusculas_map)