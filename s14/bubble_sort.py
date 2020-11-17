import random
import numpy as np
import time

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Crea una bandera que permitirá que la función
        # termine temprano si no queda nada por ordenar
        already_sorted = True

        # Empiece a mirar cada elemento de la lista uno por uno,
        # comparándolo con su valor adyacente. Con cada
        # iteración, la parte de la matriz que miras
        # encoge porque los elementos restantes ya se han
        # ordenado.

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # Si el elemento que está mirando es mayor que su
                # valor adyacente, cámbielos
                array[j], array[j + 1] = array[j + 1], array[j]

                # Como tuvo que intercambiar dos elementos,
                # establecer el indicador ʻalready_sorted` en `False` para que
                # el algoritmo no termine prematuramente
                already_sorted = False

        # Si no hubo intercambios durante la última iteración,
        # la matriz ya está ordenada y puede terminar

        if already_sorted:
            break

    return array

numeros  = []
for x in range(1000000):
        numeros.append(random.randrange(100000))

start_time = time.time()

bubble_sort(numeros)
print("--- %s seconds ---" % (time.time() - start_time))