def fib2(n): # devuelve la serie de Fibonacci hasta n

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)    # ejecutamos la función hasta 100
print(f100)         # imprimimos la lista de números
f = fib2            # creamos un nombre con la referencia a la función
print(f)            # validamos que es una función
f100_2 = f(100)     # ejecutamos la función a través del nombre referenciado
print(f100_2)       # verificamos que obtenemos el mismo valor de la función