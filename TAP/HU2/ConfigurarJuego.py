class ConfigurarJuego:

    def __init__(self):
        self.tiempoJuego = 0
        self.cantidadPreguntas = 0
    def ingresarTiempo(a):
        if a < 0:
            return False
        ConfigurarJuego.tiempoJuego = a
        return True
    def ingresarCantidadPreguntas(b):
        if b > len(ConfigurarJuego.numeros) or b < 3:
            return False
        ConfigurarJuego.cantidadPreguntas = b
        return True

