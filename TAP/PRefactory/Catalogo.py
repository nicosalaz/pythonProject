class Catalogo():
    def __init__(self):
        self.marca = ['Renault', 'Toyota']
        self.precio = [18000000, 50000000]

    def agregarCatalogo(self,marca,precio):
        self.marca.append(marca)
        self.precio.append(precio)

    def buscarPos(self,m):
        pos = 0
        conta = 0
        esta = False
        while conta < len(self.marca) and esta == False:
            if self.marca.__getitem__(conta) == m:
                esta = True
                pos = conta
        return pos
    def existeMarca(self,m):
        if m in self.marca:
            return True
        return False

    def getMarca(self,pos):
        return self.marca[pos]
    def getPrecio(self,pos):
        return self.precio[pos]