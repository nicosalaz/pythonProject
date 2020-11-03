import abc
from TAP.PatronesDeDiseño.AbstractFactory.Drink import Drink
from TAP.PatronesDeDiseño.AbstractFactory.AbstractFactory import AbstractFactory
from TAP.PatronesDeDiseño.AbstractFactory.Product import Product


class ComboUno(AbstractFactory):

    def createProduct(self):
        return Product('PopCorn',10000)
    def createDrink(self,number):
        return Drink("Coke",7000)
