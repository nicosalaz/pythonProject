a = [1, 2, 3]   # 1) a hace referencia a la lista [1, 2, 3]
b = a           # 2) b ahora hace referencia a lo que a referencia
a.append(4)     # 3) esto cambia la lista a la que a referencia
print(b)        # 4) si imprimimos entonces lo que b referencia... cambió!!
print(a)