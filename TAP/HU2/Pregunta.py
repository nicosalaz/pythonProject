class Pregunta:
    def __init__(self ,con ,defi):
        self.concepto = con
        self.definicion = defi
        self.estado = False
    def getConcepto(self):
        return self.concepto
    def getDefinicion(self):
        return self.definicion
    def getEstado(self):
        return self.estado
    def setConcepto(self,nuevo):
        self.concepto = nuevo
    def setDefinicion(self, nuevo):
        self.definicion = nuevo
    def setEstado(self, nuevo):
        self.estado =  nuevo