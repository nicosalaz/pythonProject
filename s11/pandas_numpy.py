import numpy as np
import pandas as pd

# Fijamos la semilla para un ejemplo reproducible
np.random.seed(0)

# creamos un dataframe con flotantes aleatorios
df = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
print(df)

print(df.describe())

# creamos un dataframe con enteros en un rango dado
df = pd.DataFrame(np.arange(25).reshape(5,5),columns=list('ABCDE'))
print(df)

# visualizamos algunos datos descriptivos del dataframe
print(df.describe())