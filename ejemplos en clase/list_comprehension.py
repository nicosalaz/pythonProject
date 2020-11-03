cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

print(cuadrados)

# Equivalente con compresión de listas, note que la lista no es inicializada
cuadrados2 = [x ** 2 for x in range(10)]
print(cuadrados2)