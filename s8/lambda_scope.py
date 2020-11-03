def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(1)
print(f(0))
print(f(1))