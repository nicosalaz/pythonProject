from random import randint

def quicksort(array):
    # Si la matriz de entrada contiene menos de dos elementos,
    # luego devuélvelo como resultado de la función
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Seleccione su elemento `pivote` al azar
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Los elementos que son más pequeños que el "pivote" van a
        # la lista `baja`. Elementos que son más grandes que
        # `pivot` va a la lista` high`. Elementos que son
        # igual a `pivote` ir a la lista` misma`.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # El resultado final combina la lista ordenada de "bajos"
    # con la lista `misma` y la lista` alta` ordenada
    return quicksort(low) + same + quicksort(high)

print(quicksort([8, 2, 6, 4, 5]))