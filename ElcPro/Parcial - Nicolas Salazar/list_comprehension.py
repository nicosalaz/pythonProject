num = input('numero Uno: ') # primer numero
numDos = input('numero Dos: ') # segundo segundo numero
#lista comprimida con los numeros de 1 al 1000 que pueden ser divididos por ambos numeros
numeros =[x for x in range(1,1000) if int(x) % int(num) == 0 and int(x) % int(numDos) == 0]
print(numeros)