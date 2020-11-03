import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn import linear_model

def leer():
    file = pd.read_csv("gb_consumption.csv")
    avg = np.array(file.get('Avg players'))
    gb = np.array(file.get('Gb consumption'))
    return gb,avg

def calcular(numeros):
    result,nums = leer()
    resultados =[]
    for x in numeros:
        div = result[-1]
        calculo = (x/50)*div
        resultados.append(calculo)
    return resultados


print(leer())
numeros = np.array([60,100,150])
calculos = calcular(numeros)



result,nums = leer()
plt.scatter(nums, result, color='red', marker='.', label='Sample data')
plt.plot([0,numeros[-1]],[0,calculos[-1]],color = 'green', label = 'Lineal aprox')
plt.scatter(numeros,calculos,color='blue',marker='*',label='Estimated value')
plt.legend()
plt.xlabel('Avg Players',size = 15,color = 'grey')
plt.ylabel('Gigabytes',size = 15,color = 'grey')
#plt.grid()
plt.title('Gaming Platform Provision')
plt.show()

