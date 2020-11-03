from TAP.HU2.Pregunta import  Pregunta
from TAP.HU2.ConfigurarJuego import ConfigurarJuego
class Juego:
    def __init__(self):
        self.listPreguntas = []
        self.objConfi = ConfigurarJuego()

    # def getConfigurarJuego(self):
    #
    # def getConceptos(self):



    # def puntajeConceptoAcertado(self):
    #
    # def presentarDescripcion(self):
    def getPosConcepto(self,c):
        conta = 0
        est = False
        pos = len(self.listPreguntas)+1
        if self.buscarConcepto(c):
            while conta < len(self.listPreguntas) and est == False:
                if self.listPreguntas[conta].getConcepto() == c:
                    pos = conta
                    est = True
        return pos

    def agregarConceptos(self,c,d):
        if len(c) < 3 or len(d) < 5 or self.buscarConcepto(c):
            return False
        self.objPregunta = Pregunta(c, d)
        self.listPreguntas.append(self.objPregunta)
        return True

    def buscarConcepto(self, c):
        conta = 0
        estado = False
        while conta < len(self.listPreguntas) and estado == False:
            if self.listPreguntas[conta].getConcepto() == c:
                estado = True
            conta += 1
        return estado

    def eliminarConceptos(self,c):
        pos = 0
        est = False
        if self.buscarConcepto(c):
            if self.getPosConcepto(c) < len(self.listPreguntas):
                pos = self.getPosConcepto(c)
                est = True
        self.listPreguntas.remove(self.listPreguntas[pos])
        return est


