#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from TAP.PRefactory.Concesionario import Concesionario
class TestConcesionario(unittest.TestCase):
    def setUp(self):
        self.marca = "Renault"
        self.precio = 18000000
        self.myConcesionario = Concesionario()
        
    def tearDown(self):
        print("fin")

    def test_registrarMarcaCP1(self):
        print(self.myConcesionario.registrarMarca(self.marca))
        self.assertEqual(self.myConcesionario.getCantidad(), 1)

    def test_registrarMarcaCP2(self):
        self.myConcesionario.registrarMarca(self.marca)
        self.myConcesionario.registrarMarca(self.marca)
        self.assertEqual(self.myConcesionario.getCantidad(), 2)

    def test_consultarPrecioMarcaCP3(self):
        self.myConcesionario.registrarMarca(self.marca)        
        self.assertEqual(self.myConcesionario.getPrecio(self.marca), 18000000)

    def test_consultarPrecioMarcaCP4(self):
        self.myConcesionario.registrarMarca(self.marca)        
        self.assertEqual(self.myConcesionario.getPrecio("Nisan"), "La Marca no Existe")

    def test_consultarTodasMarcasCP5(self):
        datosRes = [(self.marca, 18000000), ("Toyota", 50000000)]
        self.myConcesionario.registrarMarca(self.marca)
        self.myConcesionario.registrarMarca("Toyota")        
        datos = self.myConcesionario.getDatosMarcas()
        self.assertEqual(datos, datosRes)
        
if __name__ == "__main__":
    unittest.main()

    
    

