import random
import time

def insertion_sort(array):
    # Bucle desde el segundo elemento de la matriz hasta
    # el último elemento
    for i in range(1, len(array)):
        # Este es el elemento que queremos posicionar en su
        # lugar correcto
        key_item = array[i]

        # Inicialice la variable que se usará para
        # encontrar la posición correcta del elemento referenciado
        # por `key_item`
        j = i - 1

        # Repase la lista de elementos (la izquierda
        # porción de la matriz) y encuentre la posición correcta
        # del elemento al que hace referencia `key_item`. Haz esto solo
        # si `key_item` es más pequeño que sus valores adyacentes.
        while j >= 0 and array[j] > key_item:
            # Desplaza el valor una posición a la izquierda
            # y reposicione j para apuntar al siguiente elemento
            # (de derecha a izquierda)
            array[j + 1] = array[j]
            j -= 1

        # Cuando termine de cambiar los elementos, puede colocar
        # `key_item` en su ubicación correcta
        array[j + 1] = key_item

    return array


numeros  = []
for x in range(100000):
        numeros.append(random.randrange(100000))

start_time = time.time()

print(insertion_sort(numeros))

print("--- %s seconds ---" % (time.time() - start_time))
