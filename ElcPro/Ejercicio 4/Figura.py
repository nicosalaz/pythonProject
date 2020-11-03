import abc
import math
class Figura():
    @abc.abstractmethod
    def area(self):
        print('metodo abstracto')

class Circulo(Figura):

    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return (math.pi*(self.radio**2))

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return (self.lado**2)

class Rectangulo(Figura):
    def __init__(self,base,alt):
        self.base = base
        self.altura = alt

    def area(self):
        return (self.base*self.altura)


cuadrado = Cuadrado(2)
recatangulo = Rectangulo(2,3)
circulo = Circulo(3)

print('Area cuadrado: ',cuadrado.area())
print('Area circulo:',circulo.area())
print('Area rectangulo: ',recatangulo.area())
