class Inventario():
    def __init__(self):
        self.marcas = []

    def agregarMarca(self,marca):
        self.marcas.append(marca)

    def getMarca(self):
        return self.marcas
