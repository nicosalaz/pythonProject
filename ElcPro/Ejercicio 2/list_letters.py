letters = ['A', 'a', 'm', 'n', 'o', 'n', 'Z', 'z', 'A', 'p', 'q', 'n', 'u']
estado = False
conta = 0
for x in range(0, len(letters)):
    for y in range(0, len(letters)):
        if letters[x] == letters[y] or letters[x] == letters[y].swapcase():
            if x > y:
                estado = True
                break
            else:
                conta+=1
    if estado == False:
        print('la letra ', letters[x], 'se repite', conta, 'veces')
        conta = 0
    estado = False