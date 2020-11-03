from Tienda.Inventario import Inventario
from Tienda.Producto import Producto
import unittest

class Test_invetario(unittest.TestCase):
    def setUp(self):
        self.inventario  = Inventario()
        self.name = ' Pan'
        self.nameFake = 'Papas'
        self.price = 500
        self.amount = 10
        self.priceFake = -500
        self.amountFake = -10

    def test_addProduct(self):
        self.assertEqual(self.inventario.addProduct(self.name, self.price, self.amount), True)
        self.assertEqual(self.inventario.addProduct(self.name, self.priceFake, self.amountFake), False)
    def test_positionSearch(self):
        self.assertEqual(self.inventario.addProduct(self.name, self.price, self.amount), True)
        self.assertEqual(self.inventario.positionSearch(self.name),0)
    def test_productExist(self):
        self.assertEqual(self.inventario.addProduct(self.name, self.price, self.amount), True)
        self.assertTrue(self.inventario.productExist(self.name))
        self.assertFalse(self.inventario.productExist(self.nameFake))
    def test_deleteProduct(self):
        self.assertEqual(self.inventario.addProduct(self.name, self.price, self.amount), True)
        self.assertTrue(self.inventario.deleteProduct(self.name))
        self.assertFalse(self.inventario.deleteProduct(self.nameFake))



if __name__ == '__main__':
    unittest.main()
