from TAP.PRefactory.Catalogo import Catalogo
from TAP.PRefactory.Inventario import Inventario
class Concesionario():
    def __init__(self):
        self.catalogo = Catalogo()
        #self.inventario = Inventario()
        self.autos = list()

    def registrarCatalogo(self, marca,precio):
        self.catalogo.agregarCatalogo(marca,precio)

    def registrarMarca(self,marca):
        self.autos.append(marca)
    def getCantidad(self):
        return (len(self.autos))

    def getPrecio(self, marca):
        if self.catalogo.existeMarca(marca):
            return self.catalogo.getPrecio(self.catalogo.buscarPos(marca))
        else:
            return '"La Marca no Existe"'

    def getDatosMarcas(self):
        datos = []
        for x in range(0, len(self.catalogo.marca)):
                datos.append((self.catalogo.marca.__getitem__(x),self.catalogo.precio.__getitem__(x)))
        return datos


        

