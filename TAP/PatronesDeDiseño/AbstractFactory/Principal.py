from TAP.PatronesDeDiseño.AbstractFactory.FactoryProducer import FactoryProducer
class Principal:

    def interaccion(self):
        opc = input('Que combo desea: Combo 1 o Combo 2: ',)
        factura = []
        print('Fatura:')
        if opc == 1:
            factura = FactoryProducer.createComboUno()
        elif opc == 2:
            factura = FactoryProducer.createComboDos()

        for x in factura:
            print(x)

Principal.interaccion(Principal)