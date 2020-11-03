class Pedido:
    def __init__(self):
        self.listaProdutos = []

    def agregarProducto(self,comida,bebida):
        self.listaProdutos.append((comida,bebida))
