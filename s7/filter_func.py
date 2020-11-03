notas = [3.2, 3.8, 3.5, 4.5, 3.8, 4.0, 5.0, 2.0, 3.0, 4.7]

# Función para determinar estudiantes aprobados
def es_aprobado(nota):
    return nota > 3.5

# usando un ciclo
aprobados = []
for nota in notas:
    if es_aprobado(nota):
        aprobados.append(nota)

print(aprobados)

# usando una función filter
aprobados = list(filter(es_aprobado, notas))
print(aprobados)

