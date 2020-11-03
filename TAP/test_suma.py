import unittest
import TAP.mymodule

class TestMyModule(unittest.TestCase):
    def test_establecerTiempo(self):
        self.assertEqual(TAP.mymodule.ConfigurarJuego.establecerTiempo(12),True)
        self.assertEqual(TAP.mymodule.ConfigurarJuego.establecerTiempo(-1),False)
        self.assertEqual(TAP.mymodule.ConfigurarJuego.establecerTiempo('a'), False)
    def test_establecerNumPreguntas(self):
        self.assertEqual(TAP.mymodule.ConfigurarJuego.establecerNumPreguntas(10),)
if __name__ == '__main__':
        unittest.main()