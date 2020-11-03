# Los conjuntos se definen con sus elementos entre corchetes curvos
canasta = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# duplicados son removidos
print(sorted(canasta)[-1])
lista = list(canasta)
print(lista[1])
# validación rápida de membresía
print('orange' in canasta)
print('pineapple' in canasta)
for i,fruta in enumerate(canasta):
    print(i,fruta)

print('hola' in canasta)

