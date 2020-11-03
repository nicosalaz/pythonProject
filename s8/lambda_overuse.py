numeros = [10, 2, -3, 4, -5]

numeros_clasificados = sorted(numeros, key = lambda n: abs(n))

print(numeros_clasificados)

# abs es una función de orden superior
numeros_clasificados2 = sorted(numeros, key = abs)

print(numeros_clasificados2)
