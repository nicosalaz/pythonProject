# convierte a mayusculas los items de la lista
print(list(map (lambda x: x.upper (), ['gato', 'perro', 'vaca'])))

# devuelve solo los items de la lista que contengan la letra 'o'
print(list(filter (lambda x: 'o' in x, ['gato', 'perro', 'vaca'])))

# genera una cadena concatenada a partir de la salida de los items de la lista
from functools import reduce
print(reduce(lambda acc, x: f'{acc} - {x}', ['gato', 'perro', 'vaca']))
