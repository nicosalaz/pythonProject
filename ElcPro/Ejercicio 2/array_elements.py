numeros = [2,5,2,1,1,5,8,2,3]
aux = [numeros[0]]
estado = False
for x in range(0, len(numeros)):
    for y in range(0,len(aux)):
        if numeros[x] == aux[y]:
            estado = True
            break
    if estado == False:
        aux.append(numeros[x])
    estado = False

print(aux)