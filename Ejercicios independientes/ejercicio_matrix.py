import random

def generar_numero():
    codigo = ''         #variabale para almacenar el codigo generado
    est = False         #estado que controla el ciclo while
    while est == False:
        num = str(random.randrange(10))         #generador de numeros aleatorios entre 0 y 10
        if (str(num) in str(codigo)) == False:  #valida si el numero no existe en el codigo
            codigo+=num      #inserta el numero
        if len(codigo) == 4:        # evalua el tamaño del codigo
            est = True      # salida del ciclo
    # retrono del codigo
    return codigo

def decifrar_codigo(cod_generado):
    #variables que controlan en flujo del ciclo
    contador_ciclo = 0
    estado_encontrado = False
    #print(cod_generado)
    # ciclo para los 10 intentos
    while contador_ciclo < 10 and estado_encontrado == False:
        #variables que me cuentan los aciertos
        contador_numeros = 0
        contado_posicion = 0
        #numero ingresado por el usuario
        numeros = input('ingrese un numero de 4 digitos:', )
        for x in range(len(cod_generado)):
            for y in range(len(numeros)):
                #evalua si los numeros son iguales y las posiciones tambien
                if int(codigo_generado[x]) == int(numeros[y]) and x == y:
                    contador_numeros += 1
                    contado_posicion += 1
                #evalua si el numero solamente pertenece al codigo aunque este en otra posicion
                elif int(codigo_generado[x]) == int(numeros[y]) and x != y:
                    contador_numeros += 1
        #impresion de mensajes segun el resultado
        if contado_posicion == 0 and contador_numeros == 0:
            print('Intento no valido')
        elif contador_numeros == 4 and contado_posicion == 4:
            print('Exito')
            print('numero intentos = ',contador_ciclo)
            estado_encontrado = True
        else:
            print('Tuvo',contador_numeros,'aciertos,',contado_posicion,'en posicion correcta')
        contador_ciclo += 1
        #game over
        if contador_ciclo == 9:
            print('lo sentimos, se te acabaron los intentos')
            break


codigo_generado = generar_numero()
decifrar_codigo(codigo_generado)
