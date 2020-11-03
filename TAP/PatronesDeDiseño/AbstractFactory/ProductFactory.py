import abc
from TAP.PatronesDeDiseño.AbstractFactory.Product import Product
from TAP.PatronesDeDiseño.AbstractFactory.AbstractFactory import AbstractFactory
class ProductFactory(AbstractFactory):

    def createProduct(self,number):
        if number == 1:
            return Product("sandwich",10000)
        elif number == 2:
            return Product("hotDog", 8000)
        elif number == 3:
            return Product("Burger",10000)
        elif number == 4:
            return Product("popCorn",12000)

    def createDrink(self):
        return None
