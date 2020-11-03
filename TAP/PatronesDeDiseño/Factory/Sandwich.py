#!/usr/bin/python
#-*- coding: utf-8 -*-

from TAP.PatronesDeDiseño.Factory.Producto import Producto

class Sandwich(Producto):
    def __init__(self, nombre, precio):
        Producto.__init__(Producto,nombre, precio)
