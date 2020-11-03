import numpy as np

A = np.array([[1,1,1], #creacion de ecuaciones
             [15000,10000,5000],
             [400,300,100]])
B = np.array([60,475000,12500]) #valores de cada dato, (empleados, lineas, prograams

x, residuals, rank, s = np.linalg.lstsq(A,B)#Calculo del sistema de ecuaciones
print(x, "Masters, Seniors y Juniors ")#Impresión de resultados