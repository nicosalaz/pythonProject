class Producto:
    def __init__(self,name,unitPrice,amount):
        self.name = name
        self.unitPrice = unitPrice
        self.amount = amount
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getUnitPrice(self):
        return self.unitPrice
    def setUnitPrice(self,newUnitPrice):
        self.unitPrice = newUnitPrice
    def getAmount(self):
        return self.amount
    def setAmount(self,newAmount):
        self.amount = newAmount