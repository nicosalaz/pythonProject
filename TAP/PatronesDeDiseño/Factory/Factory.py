from TAP.PatronesDeDiseño.Factory.Perro import Perro
from TAP.PatronesDeDiseño.Factory.Sandwich import Sandwich
from TAP.PatronesDeDiseño.Factory.Crispetas import Crispetas
from TAP.PatronesDeDiseño.Factory.Gaseosa import Gaseosa
from TAP.PatronesDeDiseño.Factory.Mecato import Mecato
from TAP.PatronesDeDiseño.Factory.Nacho import Nacho

class Factory:

    def obtenerProducto(self, opcion):
        if opcion == 1:
            return Perro("Hotdog", 15000)
        elif opcion == 2:
            return Sandwich("Qbano", 15000)
        elif opcion == 3:
            return Crispetas("Crispetas", 10000)
        elif opcion == 4:
            return Gaseosa("Coke", 5000)
        elif opcion == 5:
            return Mecato("Chocolate", 2000)
        elif opcion == 6:
            return Nacho("Nachos", 10000)







