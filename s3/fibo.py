# Módulo de los números de Fibonacci

def fib(n):    # Escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # Retorna la serie Fibonacci hasta n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(100))
print(fib(100))
#Permite la ejecución desde la línea de comandos
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))