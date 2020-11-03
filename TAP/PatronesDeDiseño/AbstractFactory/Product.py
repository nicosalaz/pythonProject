class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getPrice(self):
        return self.price
    def setPrice(self,newPrice):
        self.p = newPrice