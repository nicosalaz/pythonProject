nacimientos = {'Luis': {1970,'Cali'}, 'Ana': 1982, 'Guido': 1965}  # Se crea el diccionario

print(nacimientos.items())
print(nacimientos.values())
print(nacimientos.keys())

for k, v in nacimientos.items():
     print(k, v)

for i, k in enumerate(nacimientos):
    print(i, k)

