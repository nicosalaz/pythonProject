import pandas as pd

df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
    "Allen, Mr. William Henry",
    "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Size": [50, 90, 48],
    "Sex": ["male", "male", "female"]}
)

# visualizamos la serie de la columna edad
print(df["Age"])

# o la creamos directamente
ages = pd.Series([22, 35, 58], name="Age")
print(ages)

# podemos acceder a metodos del dataframe o de la serie como tal
print(df["Age"].max())
print(ages.max())

# visualizamos algunas estadisticas de las columnas numéricas
print(df.describe())
print()
print(ages.describe())