cadenas = ['decir','balneario','habria','cabria','seria','abanico','quesera','mentir'] #lista de cadenas a evaluar
listaDeCadenas = {} #donde se a va a almacenar la evalucacion de cadenas
comparadas = [] # lista auxiliar para almacenar comparaciones
letters = [] #lista auxiliar para evitar que se repitan la evaluacion de letras
aux = [] #lista auxiliar para impirmir los verdaderos resultados

# esta funcion es la encargada de evaluar palabra por palabra y guardar los resultados en la lista auxiliar
def palabrasSimilares(cadenas):
    mayor = 0 #variable para almacenar las similitudes entre palabras
    for x in range(0,len(cadenas)):
        for y in range(x,len(cadenas)):
            if cadenas[x] != cadenas[y] : #condicion para que no se evaluen las palabras iguales
                mayor = similitud(cadenas[x],cadenas[y])
                comparadas.append([mayor,cadenas[x],cadenas[y]]) #almacenaiento a la lista auxiliar
    return comparadas
#retorna el numero de similitudes entre dos palabras
def similitud(p1,p2):
    num = 0
    for x in range(0,len(p1)):
        for y in range(0,len(p2)):
            # validacion para que ambas letras existan en ambas palabras y no se hayan evaluado anteriormente
            if (p1[x] in p1) == True and (p1[x] in p2) == True and (p1[x] in letters) == False:
                #validacion para sumar la cantidad correcta de veces que se repite una letra en ambas palabras
                if p1.count(p1[x]) < p2.count(p1[x]):
                    num += p1.count(p1[x])
                else:
                    num+= p2.count(p1[x])
                letters.append(p1[x])#me agrega las letras ya evaluadas para no repetirlas
    letters.clear() #setea la lista para evaluar nuevas palabras
    return num

def imprimir():
    #organiza los registros de mayor a menor
    comparadas.sort()
    comparadas.reverse()
    for c in range(0,len(comparadas)):
        pos = str([comparadas[c].__getitem__(1), comparadas[c].__getitem__(2)])
        #coloca el resgistro mayor a menor en el diccionario
        if (comparadas[c].__getitem__(1) in aux) == False and (comparadas[c].__getitem__(2) in aux) == False:
            listaDeCadenas[pos] = comparadas[c].__getitem__(0)
            #agrega a una lista auxiliar para no repetir datos y colocar el mayor
            aux.append(comparadas[c].__getitem__(1))
            aux.append(comparadas[c].__getitem__(2))
    return listaDeCadenas



palabrasSimilares(cadenas)
listaDeCadenas = imprimir()
print(listaDeCadenas)