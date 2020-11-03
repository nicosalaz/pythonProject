import numpy as np
import matplotlib.pyplot as plt

x=0     #Declarar variable x

func=input("digite la funcion:")        #Solicita la funcion
a,b = input("digite el dominio de x:").split()      #solicicta el dominio de la funcion
intervalo = input("Digite el intervalo:")       #solicita el intervalo


#Captura los errores para cada dato ingresado
try:
    eval(func)
except:
    print("Error: Funcion No valida")

try:
    float(a)
except:
    print("Error: Limite Inferior No Valido")

try:
    float(b)
except:
    print("Error: Limite Superior No Valido")

try:
    float(intervalo)
except:
    print("Error: intervalo No Valido")

def f(x):       #Definicion de la funcion
    return eval(func)

x = np.arange(float(a),float(b),float(intervalo))       #Definiicon de x

plt.plot(x, f(x), label="Funcion " + func)      #Generar Tabla
plt.xlabel("Eje $x$")                           #Nombre del Eje x
plt.ylabel("$f(x)$")                            #Nombre del Eje y
plt.legend()                                    #Leyenda de la grafica
plt.title("Función $f(x)$")                     #Titulo Grafica
plt.grid()                                      #Grilla de la tabla
plt.show()                                      #Mostrar Grafica
