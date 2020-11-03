import numpy as np
import matplotlib.pyplot as plt

funcion = input('Digite la funcion a graficar:',)
print('limites en X:')
limiteInferior,limiteSup =input('Ingresa los limites en x ',).split()
intervalo = float(input('Digite el intervalo:',))

try:
    int(limiteInferior)
    int(limiteSup)
    float(intervalo)
except Exception as a:
    print('ingresaste un valor incorrecto', type(a).__name__)

x = np.arange(int(limiteInferior),int(limiteSup),float(intervalo))
try:
    eval(funcion)
except Exception as e:
    print('ingresaste la funcion incorrecta, tipo error:',type(e).__name__)
    raise

def f(x):
    return eval(funcion)

def graficar(func,x):
    plt.plot(x,f(x),color = 'blue',label = 'funcion')
    plt.xlabel('Eje x')
    plt.ylabel('f(x)')
    plt.title('Función f(x) = '+func)
    plt.legend()
    plt.grid()
    plt.show()


graficar(funcion,x)
