def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
        print("-" * 40)
    for c in palabrasclaves:
        print(c, ":", palabrasclaves[c])

ventadequeso("Limburger", "Es muy liquido, sr.",
 "Realmente es muy muy liquido, sr.",
 cliente="Juan Garau",
 vendedor="Miguel Paez",
 puesto="Venta de Queso Argentino")