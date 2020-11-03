class ConfigurarJuego():
    tiempoJuego = 0
    numPreguntas = 0
    def establecerTiempo(tiempo):
        if type(tiempo) != int or tiempo < 0:
            return False
        tiempoJuego = tiempo
        return True
    def establecerNumPreguntas(numero):
        if type(numero) != int or numero < 0:
            return False
        numPreguntas = numero
        return True

