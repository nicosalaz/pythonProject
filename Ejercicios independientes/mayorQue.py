from datetime import datetime
import time
# def max(a,b):
#     if a > b:
#         return a
#     return b
# print('el numero mayor es ', max(8,5))
#
# def max_tres(a,b,c):
#     if a > b:
#         return a
#     elif b > c:
#         return b
#     return c
# print('el numero mayor es',max_tres(1,5,3))
#
# def longTupla(*numeros):
#     conta = 0
#     for x in numeros:
#         conta+=1
#     return conta
# print(longTupla(1,2,3,4))
#
# def esVocal(a):
#     if a == 'a' or a == 'A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U':
#         return True
#     return False
# print(esVocal('v'))
# def suma(numeros):
#     result = 0
#     for x in numeros:
#         result += x
#     return result
# def multi(numeros):
#     res = 1
#     for y in numeros:
#         res *= y
#     return res
#
# numeros = [1,2,3,4]
# print('el resultado de la suma y multiplicacion de', numeros,'es','suma',suma(numeros),'multiplicacion',multi(numeros))

# def inversa (cadena):
#     invertida = ""
#     conta = len(cadena)
#     indice = -1
#     while conta >= 1:
#         invertida += cadena[indice]
#         indice-=1
#         conta -=1
#     return invertida
#
# frase = inversa('oro')
# print(frase)
#
# def esPalindromo(cadena):
#     if cadena == inversa(cadena):
#         return 'es palindromo'
#     return 'no es palindromo'
#
# print(esPalindromo('hola'))

# def listasIguales(lista1,lista2):
#     for x in range(0, len(lista1)):
#         for y in range(0,len(lista2)):
#             if lista1[x] == lista2[y]:
#                 return True
#     return False
#
# lista1 = [1,2,3,4]
# lista2 = [4,6,7,8]
# print(listasIguales(lista1,lista2))
# def imprimirVarios(n,c):
#     print(c * n)
# imprimirVarios(5,'x')

# def histograma(c,nums):
#     for x in nums:
#         print(c * x)
#
# lista =[3,5,6]
# histograma('*',lista)
# def max_in_list(num):
#     conta = 0
#     for x in num:
#        if conta < x:
#            conta = x
#     return conta
#
# lista = [8,3,5]
# print(max_in_list(lista))
#
# def mas_larga(cadenas):
#     mayor = 0
#     cadena = ""
#     for x in cadenas:
#         if mayor < len(x):
#             mayor = len(x)
#             cadena = x
#     return cadena
#
# lista = ['hola', 'nicolas','veronica']
# print(mas_larga(lista))

# def filtrar_palabras(cadenas,n):
#     for x in cadenas:
#         if n < len(x):
#             print(x)
#
# lista = ['hola', 'nicolas','veronica']
# filtrar_palabras(lista,8)

# def borrar(lista, num):
#     pos = 0
#     conta = 0
#     est = False
#     while conta < len(lista) and est == False:
#         if lista[conta] == num:
#             lista.remove(lista[conta])
#             pos = conta
#             est =  True
#         conta+=1
#     return pos
#
# lista = [1,2,3]
# print(borrar(lista,3))

# def cronometro(hora,min,sec):
#     h = int(hora)
#     m = int(min)
#     s = int(hora)
#     print('incio:')
#     for h in range(0,24):
#         for m in range(0,60):
#             for s in range(0,60):
#                 print(h,':',m,':',s)
#                 time.sleep(1)
# hora = time.strftime('%H')
# minu = time.strftime('%M')
# sec = time.strftime('%S')
#
# cronometro(hora,minu,sec)
# lista = list()
# name = 'Nicolas'
# lName = 'Salazar'
# documento = 1005871501
# cliente = (name,lName,documento)
# c2 = ('Vanessa','Calixto',12345678)
# lista.append(cliente)
# lista.append(c2)
# del lista[1]
# print(lista)

# cadena = input('Digite una cadena: ',)
# conta = 0
# for x in cadena:
#     if x.isupper():
#         conta+=1
# print('la palabra', cadena ,'tiene',conta,'letras mayusculas')
# anioActual = input('digite el año actual:',)
# personas = list()
# for x in range(0,2):
#     nombre = input('digite su nombre:',)
#     nacimiento = input('digite su fecha de nacimiento:')
#     personas.append([nombre,nacimiento])
# for x in personas:
#     edad = int(anioActual) - int(x[1])
#     print('la edad de ',str(x[0]),'es',edad,'años')
# def riman(cadena1,cadena2):
#     conta = -1
#     contador = 0
#     for x in range(0,3):
#         if cadena1[conta] == cadena2[conta]:
#             contador+=1
#         conta-=1
#     if contador == 3:
#         print('si riman')
#     elif contador == 2:
#         print('riman un poco')
#     else:
#         print('no riman')
# riman('ojo', 'majo')
