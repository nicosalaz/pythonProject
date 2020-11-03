numeros=[x for x in range(0,30)]
def aprobado(num):
    if num % 2 != 0:
        return num

impares =map(lambda x: aprobado(x),numeros)

print(impares)