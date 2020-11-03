# Una función generadora
def mi_generador():
    n = 1
    print('Primera impresión')
    yield n

    n += 1
    print('Segunda impresión')
    yield n

    n += 1
    print('Tercera impresión')
    yield n


a = mi_generador()
next(a)
next(a)
next(a)
print(a)

