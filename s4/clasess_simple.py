class MyClass:
    """Un ejemplo sencillo de una clase"""
    i = 12344

    def __init__(self):
        self.i = self.i + 1

    def f(self):
        return 'Hola Mundo! ' + str(self.i)

x = MyClass()

x.f()           # Accediendo al metodo f
print(x.f())    # Imprimiendo el valor retornado por el método f
x.i = 5         # Asignando un valor al atributo i de la clase
print(x.f())    # Imprimiento el nuevo valor a retornar del método f
f = x.f()       # Creando una referencia a un método de una clase
print (f)