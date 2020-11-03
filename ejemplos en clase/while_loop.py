x = 3

while x < 10:
    if x < 7:
        x += 2
        continue
    x = x + 1
    print ('Aún dentro del ciclo.',x)
    if x == 9:
        print("En el break")
        #break
print ('Fuera del ciclo.')

# Cuantas veces imprimirá 'Aún dentro del ciclo' ?