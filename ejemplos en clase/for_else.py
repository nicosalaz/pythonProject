# Encuentra los numeros primos hasta el 9

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
    else:
        # sigue el bucle sin encontrar un factor
        print(n, 'es un numero primo')