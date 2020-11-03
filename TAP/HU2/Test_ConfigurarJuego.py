import unittest
from TAP.HU2.ConfigurarJuego import ConfigurarJuego

class Test_ConfigurarJuego(unittest.TestCase):
    def test_ingresarTiempo(self):
        self.assertEqual(ConfigurarJuego.ingresarTiempo(5),True)
        self.assertEqual(ConfigurarJuego.ingresarTiempo(-10), False)
    def test_ingresarCantidadPreguntas(self):
        self.assertEqual(ConfigurarJuego.ingresarCantidadPreguntas(3),True)
        self.assertEqual(ConfigurarJuego.ingresarCantidadPreguntas(5),True)
        self.assertEqual(ConfigurarJuego.ingresarCantidadPreguntas(2),False)
        self.assertEqual(ConfigurarJuego.ingresarCantidadPreguntas(6),False)


if __name__ == '__main__':
        unittest.main()