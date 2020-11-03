from itertools import *

contador = 0

for elemento in cycle("Python"):
    print(elemento, end = ' ')
    contador += 1

    if contador == 12:
        break