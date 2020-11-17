import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def leerArchivo():
    datos = pd.read_csv("gb_consumption.csv")
    x = np.array(datos.get('Avg players'))
    y = np.array(datos.get('Gb consumption'))
    return x,y

#def valores():
conservador = float(input("Ingrese un valor conservador: "))
realista = float(input("Ingrese un valor realista: "))
optimista = float(input("Ingrese un valor optimista: "))

x, y = leerArchivo()

plt.scatter(x,y,color ="red")
plt.grid()
plt.show()


