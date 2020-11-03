import abc
class AbstractFactory():
    @abc.abstractmethod
    def createProduct(self,number):
        "create products"

    @abc.abstractmethod
    def createDrink(self, number):
        "create Combos"