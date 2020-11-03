from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

def mult_acumulada(primero, segundo):
    return primero * segundo

result = reduce(mult_acumulada, numeros)
print(result)

# argumento opcional para indicar el argumento con el cual se
# hace la primera invocación
result2 = reduce(mult_acumulada, numeros, numeros[5])
print(result2)