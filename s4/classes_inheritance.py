class Perro:

    especie = 'Canino'         # Variable compartida por todas las instancias

    def __init__(self, name):
        self.nombre = name    # Variable de instancia única a cada instancia

class PerroCasero(Perro):

    def duerme(self):           # Metodo especial solo de la clase heredada
        for i in range(100000000):
            pass

d = Perro('Fido')
f = PerroCasero('Puppy')

print(d.nombre + " es un " + d.especie)
f.duerme()
print(f.nombre + " es un " + f.especie)
