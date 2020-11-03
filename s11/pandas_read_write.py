import numpy as np
import pandas as pd

# leemos el archivo de datos csv
titanic = pd.read_csv("titanic.csv")
print(titanic)

# inspeccionamos los tipos de datos cargados
print(titanic.dtypes)
print()
# Observamos los primeros n datos
print(titanic.head(8))

# observamos un resumen técnico del dataframe
print(titanic.info())

# guardamos el dataframe de vuelta en formato excel
titanic.to_csv('titanic2.csv', index=False)
