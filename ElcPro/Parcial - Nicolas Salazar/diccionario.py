letters = ['A','a','m','n','o','n','Z','z','A','p','q','n','u'] #lista de lestras
dict = {} #diccionario donde se va a almacenar los resultados
estado = False
conta = 0
for x in letters:
    for y in letters:
        #valida que me las letas sea iguales, ya sean mayusculas o no
        if x == y or x.swapcase() == y:
            #valida que no se este evaluando una letra que ya fue evaluada
            if x.swapcase() in dict or x in dict:
                estado = True
                break
            else:
                conta+=1
    #valida si no se a evaluado y la agerga al diccionario
    if estado == False:
            dict[x] = conta
    conta = 0
    estado = False
print(dict)
