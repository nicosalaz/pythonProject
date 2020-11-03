from TAP.PatronesDeDiseño.AbstractFactory.Product import Product
class PopCorn(Product):
    def __init__(self, name, price):
        Product.__init__(Product, name, price)