nacimientos = {'Luis': 1970, 'Ana': 1982}  # Se crea el diccionario inicial
nacimientos['Guido'] = 1965     # Se agregan entradas (items) al diccionario

print(nacimientos)
print(nacimientos['Luis'])

del nacimientos['Ana']          # Se elimina un item
nacimientos['Lucy'] = 1999,'Octurbe'      # Se agrega un nuevo item

print(list(nacimientos))        # Se pasa a una lista
print(sorted(nacimientos))      # Se ordenan los items
print('Guido' in nacimientos)   # Se pregunta por un item en el diccionario
print(nacimientos)
