try:
    i = int(input('Digita un número menor a 10: '))
    if i > 10:
        raise NameError(str(i)+' es un numero mayor o igual a 10')
except NameError:
    raise
except:
    print('Error inesperado!')
finally:
    print('Gracias por intentarlo...nos vemos pronto')