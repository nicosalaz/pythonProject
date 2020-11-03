import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(48).reshape(8,6),columns=list('ABCDEF'))
print(df)

df.iloc [:: 2,0] = np.nan # en la columna 0, establece elementos con índices 0,2,4, ... a NaN
df.iloc [:: 4,1] = pd.NaT # en la columna 1, establece elementos con índices 0,4, ... a np.NaT
df.iloc [: 3,2] = 'nan' # en la columna 2, establezca elementos con índice de 0 a 3 a 'nan'
df.iloc [:, 5] = None # en la columna 5, establezca todos los elementos en Ninguno
df.iloc [5 ,:] = None # en la fila 5, establezca todos los elementos en Ninguno
df.iloc [7 ,:] = np.nan # en la fila 7, establezca todos los elementos en NaN

print(df)