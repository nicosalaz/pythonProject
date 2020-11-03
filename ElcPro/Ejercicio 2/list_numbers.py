listaUno = [2,5,2,1,1,5,8,2,3]
listaDos = [4,2,7,5,9,1]
aux = []
estado = False
print('los numeros que estan en ambas listas son:')
for x in range(0,len(listaDos)):
    for y in range(0,len(listaUno)):
        if listaDos[x] == listaUno[y] and estado == False:
            estado = True;
    if estado == True:
        print(listaDos[x])
    else:
        aux.append(listaDos[x])
    estado = False

print('los numeros que solo aparecen en la segunda lista son:')
print(aux)