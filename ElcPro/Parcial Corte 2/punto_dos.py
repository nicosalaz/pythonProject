import numpy as np
import matplotlib.pyplot as plt

#pedimos los valores a evaluar
funcion = input('Digite la funcion a graficar:',)
print('limites en X:')
limiteInferior,limiteSup =input('Ingresa los limites en x ',).split()
intervalo = float(input('Digite el intervalo:',))

#capturamos los erroes en caso de que hayan para los valores ingresdos
try:
    int(limiteInferior)
    int(limiteSup)
    float(intervalo)
except Exception as a:
    print('ingresaste un valor incorrecto', type(a).__name__)
#declaramos arreglo con los datos que ingreso el usuario para graficar
x = np.arange(int(limiteInferior),int(limiteSup),float(intervalo))
#capturamos los errores que pueda generar la evaluacion de la funcion
try:
    eval(funcion)
except Exception as e:
    print('ingresaste la funcion incorrecta, tipo error:',type(e).__name__)
    raise

#graficamos con la info ingresada por el usuario.
def graficar(func,x):
    plt.plot(x,eval(func),color = 'blue',label = 'funcion')
    plt.xlabel('Eje x')
    plt.ylabel('f(x)')
    plt.title('Función f(x) = '+func)
    plt.legend()
    plt.grid()
    plt.show()


graficar(funcion,x)
