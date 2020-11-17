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

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # Si la matriz de entrada contiene menos de dos elementos,
    # se devuélven como resultado de la función
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Ordena la matriz dividiendo recursivamente la entrada
    # en dos mitades iguales, clasificando cada mitad y fusionándolas
    # en el resultado final
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

print(merge_sort([8, 2, 6, 4, 5]))