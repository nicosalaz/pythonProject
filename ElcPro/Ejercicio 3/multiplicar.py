def multi(*numeros):
    resultado = 0
    if len(numeros) >= 2:
        resultado = numeros[0]*numeros[1]
    for x in range(2,len(numeros)):
        resultado += numeros[x]
    return resultado

print(multi(2,3,5))