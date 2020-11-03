#!/usr/bin/python
#-*- coding: utf-8 -*-

class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio =   precio

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getInfo(self):
        info = self.nombre+" "+str(self.precio)
        return info