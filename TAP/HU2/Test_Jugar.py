from TAP.HU2.Juego import Juego
import unittest
class Test_Jugador(unittest.TestCase):

    def setUp(self):
        self.auxConBad = "a"
        self.auxDefBad = "hola"
        self.auxConGood = 'modelo'
        self.con = 'concepto'
        self.defi = 'definicion'
        self.pregunta = Juego()

    def test_agregarConceptos(self):
        self.assertEqual(self.pregunta.agregarConceptos(self.con,self.defi),True)
        self.assertEqual(self.pregunta.agregarConceptos(self.con,self.defi),False)
        self.assertEqual(self.pregunta.agregarConceptos(self.auxConBad,self.defi),False)
        self.assertEqual(self.pregunta.agregarConceptos(self.con,self.auxDefBad),False)

    def test_buscarConcepto(self):
        self.assertEqual(self.pregunta.agregarConceptos(self.con,self.defi),True)
        self.assertEqual(self.pregunta.buscarConcepto(self.con),True)
        self.assertEqual(self.pregunta.buscarConcepto(self.auxConGood),False)

    def test_eliminarConcepto(self):
        self.assertEqual(self.pregunta.agregarConceptos(self.con, self.defi), True)
        self.assertEqual(self.pregunta.elminarConcepto(self.con),True)
        self.assertEqual(self.pregunta.eliminarConcepto(self.auxConGood),False)







if __name__ == '__main__':
    unittest.main()