class Perro:

    especie = 'Canino'         # Variable compartida por todas las instancias

    def __init__(self, name):
        self.nombre = name    # Variable de instancia única a cada instancia

d = Perro('Fido')
e = Perro('Buddy')

print(d.nombre + " es un " + d.especie)
print(e.nombre + " es un " + e.especie)

