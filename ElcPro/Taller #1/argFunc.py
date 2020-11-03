def condicionPorParametro(*numeros, condi):
    for num in numeros:
        if condi:
            print(num)

condicion = 'num < 5'
numeros = [1,2,3,4,5,6,7,8,9]
condicionPorParametro(numeros,condicion)
