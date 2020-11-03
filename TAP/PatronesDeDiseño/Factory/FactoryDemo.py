from TAP.PatronesDeDiseño.Factory.Factory import Factory

class FactoryDemo:

    def main(self):
        Factura=[]
        estado = True
        total = 0
        while(estado):
            opcion = input("Seleccione Producto: 1)Perro 2)Sandwich 3)Crispetas 4)Gaseosa 5)Mecato 6)Nachos\n")
            producto = Factory.obtenerProducto(Factory, int(opcion))
            cantidad = input("digite la cantidad a comprar\n")
            Factura.append((producto.getNombre(), cantidad, producto.getPrecio()*int(cantidad)))
            opcion2 = input("Desea seguir comprando? S/N\n")
            if opcion2 == "s":
                estado=True
            elif opcion2 == "n":
                estado=False
        print('Factura:')
        for x in Factura:
            print('producto:', x[0],'| cantidad:',x[1],'| precio:',x[2])

        for i in range(0,len(Factura)):
            total = total+ Factura[i][2]

        print("El valor total a pagar es ",total)

FactoryDemo.main(FactoryDemo)
