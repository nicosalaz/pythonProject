funcion_orden_superior = lambda x, func: x + func(x)

print(funcion_orden_superior(3, lambda x: x * x))
