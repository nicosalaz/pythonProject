import pandas as pd
import numpy as np

np.random.seed(123)
x = np.random.standard_normal(4)
y = range(4)

# creación del dataframe a partir de un diccionario
df = pd.DataFrame({'X':x, 'Y':y})
print(df)

# creación del dataframe a partir de una lista de tuplas
data = [
('p1', 't1', 1, 2),
('p1', 't2', 3, 4),
('p2', 't1', 5, 6),
('p2', 't2', 7, 8),
('p2', 't3', 2, 8)
]
df = pd.DataFrame(data)
print(df)

# creación del dataframe a partir de un diccionario de listas
df = pd.DataFrame({'A' : [1, 2, 3, 4], 'B' : [4, 3, 2, 1]})
print(df)
df = pd.DataFrame(data)
print(df)