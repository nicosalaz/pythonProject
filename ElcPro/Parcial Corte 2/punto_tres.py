import numpy as np

categorias = ['Master','Senior','Junior']

#creamos la lista con las ecuaciones
valores = np.array([[1,1,1],
                    [15000,10000,5000],
                    [400,300,100]])
#creamos la lista de los resultados
result = np.array([60,475000,12500])
#usamos la libreria linalg para resolver le ecuacion
x, residuals,rank,s= np.linalg.lstsq(valores,result)
#imprimirmos los resultados
for idx in range(0,3):
    print(categorias[idx],'\t',round(x[idx]))

