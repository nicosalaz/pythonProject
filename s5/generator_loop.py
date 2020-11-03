# Generador implementado con un ciclo

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# Ciclo que devuelve una cadena al revés
for char in rev_str("hola"):
    print(char)