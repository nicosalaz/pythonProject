from Tienda.Producto import Producto

class Inventario:

    def __init__(self):
        self.listProductos = list()
        self.initial_products()



    def initial_products(self):
        p1 = Producto('Papas',2000,10)
        self.listProductos.append(p1)
        p2 = Producto('Gaseosa',3000,10)
        self.listProductos.append(p2)
        p3 = Producto('Paleta',1500,10)
        self.listProductos.append(p3)
    def addProduct(self,name,price,amount,tree):
        if len(name) > 0 and len(price) > 0 and len(amount) > 0:
            aux = Producto(name,price,amount)
            self.listProductos.append(aux)
            self.getProducts(tree)

    def positionSearch(self,name):
        est = False
        conta = 0
        pos = 0
        if self.productExist(name):
            while conta < len(self.listProductos) and est == False:
                if name == self.listProductos[conta].getName():
                    est = True
                    pos = conta
                conta+=1
        return pos
    def productExist(self,name):
        existe = False
        est = False
        conta = 0
        while conta < len(self.listProductos) and est == False:
            if name == self.listProductos[conta].getName():
                existe = True
                est = True
            conta+=1
        return existe
    def deleteProduct(self,tree):
        try:
            tree.item(tree.selection())['text']
        except IndexError as e:
            print('selecione algun producto')
            return
        name = str(tree.item(tree.selection())['text'])
        if self.productExist(name):
            pos = self.positionSearch(name)
            del self.listProductos[pos]
        self.getProducts(tree)
    def getProducts(self,tree):
        pos = 1
        aux = tree.get_children()
        for x in aux:
            tree.delete(x)
        for element in self.listProductos:
            tree.insert('',len(self.listProductos),text=element.getName(),values=(element.getUnitPrice(),element.getAmount()))
            pos+=1
    def validateExistence(self):
        for product in self.listProductos:
            if product.getAmount() == 0 or product.getAmount() < 0:
                del product
    def getInfo(self,tree,edit_view):
        name = tree.item(tree.selection())['text']
        valores = tree.item(tree.selection())['values']
        edit_view(str(name),str(valores[0]),str(valores[1]))
    def updateProduct(self,tree,newName,newPrice,newAmount,edit_view):
        name = tree.item(tree.selection())['text']
        pos = self.positionSearch(name)
        self.listProductos[pos].setName(newName)
        self.listProductos[pos].setUnitPrice(newPrice)
        self.listProductos[pos].setAmount(newAmount)
        self.getProducts(tree)
        edit_view.destroy()





    

