def merge(left, right):
    # Si la primera matriz está vacía, entonces no es necesario
    # para fusionar, y puede devolver la segunda matriz como resultado
    if len(left) == 0:
        return right

    # Si la segunda matriz está vacía, entonces no es necesario
    # para fusionar, y puede devolver la primera matriz como resultado
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Ahora revise ambas matrices hasta que todos los elementos
    # conviértalo en la matriz resultante
    while len(result) < len(left) + len(right):
        # Los elementos deben ordenarse para agregarlos al
        # matriz resultante, por lo que debe decidir si desea obtener
        # el siguiente elemento de la primera o segunda matriz
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # Si llega al final de cualquiera de las matrices, puede
        # agregue los elementos restantes de la otra matriz a
        # el resultado y romper el ciclo
        if index_right == len(right):
            result += left[index_left:]
            break

def insertion_sort_modified(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Bucle desde el elemento indicado por
    # `left` hasta el elemento indicado por` right`
    for i in range(left + 1, right + 1):
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
        # si el `key_item` es más pequeño que sus valores adyacentes.
        while j >= left and array[j] > key_item:
            # Desplaza el valor una posición a la izquierda
            # y reposicione `j` para apuntar al siguiente elemento
            # (de derecha a izquierda)
            array[j + 1] = array[j]
            j -= 1

        # Cuando termine de mover los elementos, coloque
        # el `key_item` en su ubicación correcta
        array[j + 1] = key_item

    return array


def timsort(array):
    min_run = 32
    n = len(array)

    # Empiece por cortar y clasificar pequeñas porciones del
    # arreglo de entrada. El tamaño de estos cortes se define por
    # su tamaño de `min_run`.
    for i in range(0, n, min_run):
        insertion_sort_modified(array, i, min((i + min_run - 1), n - 1))

    # Ahora puede comenzar a fusionar los sectores ordenados.
    # Empiece desde `min_run`, duplicando el tamaño en
    # cada iteración hasta que supere la longitud de
    # la matriz.
    size = min_run
    while size < n:
        # Determine las matrices a fusionarse
        for start in range(0, n, size * 2):
            # Calcule el `punto medio` (donde termina el primer arreglo
            # y el segundo comienza) y el ʻendpoint` (donde
            # termina el segundo arreglo)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Fusionar los dos subarreglos.
            # El arreglo `left` debe ir de` start` a
            # `midpoint + 1`, mientras que el arreglo` right` debería
            # ir de `midpoint + 1` a ʻend + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finalmente, vuelva a colocar el arreglo fusionado
            array[start:start + len(merged_array)] = merged_array

        # Cada iteración debe duplicar el tamaño de sus matrices
        size *= 2

    return array

print(timsort([8, 2, 6, 4, 5]))