for x in range(10):
    if x > 7:
        x += 2
        continue
    x = x + 1
    print ('Aún dentro del ciclo.')
    if x == 7:
        break
print ('Fuera del ciclo.')