names = ('Ana', 'Juan', 'Pedro', 'Maria')
print('Digite el nombre que desea buscar: ')
name = input('User:')
if((name in names)):
    print(name, 'si existe')
else:
    print(name, 'no existe')
