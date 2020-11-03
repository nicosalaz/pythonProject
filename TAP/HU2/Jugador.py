class Jugador:
    def __init__(self,nomJu):
        self.nombreJugador = nomJu
        self.tiempoFinal = 0
        self.puntajeFinal = 0
        self.cantidadConceptosAcertado = 0
    def getNombreJugador(self):
        return self.nombreJugador
    def setPuntajeFinal(self,a):
         self.puntajeFinal = a
    def getPuntajeFinal(self):
        return self.puntajeFinal
    def setTiempoFinal(self, a):
        self.tiempoFinal = a
    def getTiempoFinal(self):
        return self.tiempoFinal
    def setCantidadDeConceptosAcertados(self, a):
        self.cantidadConceptosAcertado = a
    def getCantidadDeConceptosAcertados(self):
        return self.cantidadConceptosAcertado
    #def intoString(self):

