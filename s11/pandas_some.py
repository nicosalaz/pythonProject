import numpy as np
import pandas as pd

# leemos el archivo de datos csv
titanic = pd.read_csv("titanic.csv")

age_sex = titanic[["Age", "Sex"]]
print(age_sex)

# obtenemos solo los pasajeros mayores de 35 años
above_35 = titanic[titanic["Age"] > 35]
print(above_35)

# visualizamos solo los 10 primeros...
print(above_35.head(10))

# imprimimos solo los pasajeros de 2da y 3ra clase
print(titanic[titanic["Pclass"].isin([2, 3])])

# imprimimos pasajeros cuya cabina es conocida
#print(titanic[titanic["Cabin"]])
print(titanic[titanic["Cabin"].notna()])