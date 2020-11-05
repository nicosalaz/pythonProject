import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def leer():#lee el archivo de excel y guarda la info en arreglos
    file = pd.read_csv("gb_consumption.csv")
    avg = np.array(file.get('Avg players'))
    gb = np.array(file.get('Gb consumption'))
    return gb,avg

def calcular(numeros):#calcula el consumo con los valores pasados por parametro
    result,nums = leer()
    resultados =[]
    div = result[-1]
    for x in numeros:
        calculo = (x/len(nums))*div
        resultados.append(calculo)
    return resultados



result,nums = leer() # resultados obtenidos del archivo
inf = int(input('dato Conservador: ',))#datos ingresados por el usuario
med = int(input('dato Realista: ',))
sup = int(input('dato Optimista: ',))
numeros = np.array([inf,med,sup])#arreglo con esta info
calculos = calcular(numeros)#retrono de los valores estimados de consumo
new_nums = np.append(nums,numeros)#arrego con toda la info de jugadores
new_result = np.append(result,calculos)#arreglo con toda la info de consumo
p = np.polyfit(new_nums,new_result,1)#ajuste polinomial de minimos cuadrados
f = np.poly1d(p)#llamamos a f(x)



#graficamos
plt.plot(new_nums,f(new_nums),color = 'green', label = 'Lineal aprox')
plt.plot(nums, result, '.' , color='red', label='Sample data')
plt.scatter(numeros,calculos,color='blue',marker='*',label='Estimated value')
plt.legend()
plt.xlabel('Avg Players',size = 15,color = 'grey')
plt.ylabel('Gigabytes',size = 15,color = 'grey')
plt.grid()
plt.title('Gaming Platform Provision')
plt.show()

