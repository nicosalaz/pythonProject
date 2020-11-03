letters = ['A','a','m','n','o','n','Z','z','A','p','q','n','u']
dict = {}
estado = False
conta = 0
for x in range(0, len(letters)):
    for y in range(0, len(letters)):
        if letters[x] == letters[y]:
            if x > y:
                estado = True
                break
            else:
                conta+=1
    if estado == False:
            dict[letters[x]] = conta
            conta = 0
    estado = False
print(dict)