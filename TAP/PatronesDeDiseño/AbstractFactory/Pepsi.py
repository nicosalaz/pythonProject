from TAP.PatronesDeDiseño.AbstractFactory.Drink import Drink
class Pepsi(Drink):
    def __init__(self, name, price):
        Drink.__init__(Drink, name, price)