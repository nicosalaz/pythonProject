#!/usr/bin/python
#-*- coding: utf-8 -*-

from TAP.PatronesDeDiseño.Factory.Producto import Producto

class Gaseosa(Producto):
    def __init__(self, nombre, precio):
        Producto.__init__(Producto,nombre, precio)
