x = int(input("Ingresa un entero, por favor: "))

# Ingresa un numero entero, por favor:
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Unidad')
else:
    if x > 3:
        print('Mayor que tres')
    else:
        print('Es 2 o 3')
