# Combina dos listas sin elementos iguales
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

# Mucho más sencillo con compresión de listas
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])