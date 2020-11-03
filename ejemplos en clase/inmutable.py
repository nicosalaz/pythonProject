# Elementos inmutables
x = 3       #  1) Crea 3, nombre x se refiere a 3
y = x       #  2) Crea nombre y, se refiere a 3.
y = 4       #  3) Crea referencia a 4. Cambia a y.
print(x)    #  4)  No hay efecto sobre x, aún hace referencia a 3.
print(y)    #4
