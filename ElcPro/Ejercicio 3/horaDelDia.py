import time
def saludar(func):
    def imprimir():
        print(func())
        return 'hola'
    return imprimir

@saludar
def buenosDias():
    return "buenos dias"
@saludar
def buenasTardes():
    return "Buenas Tardes"
@saludar
def buenasNoches():
    print("Buenas noches")
    return hora

hora = time.strftime("%H")

if int(hora) > 0 and int(hora) < 12:
   print(buenosDias(),'son las ',int(hora))
elif int(hora) >= 12 and int(hora) < 19:
     print(buenasTardes())
elif int(hora) >= 19 and int(hora) <= 24:
     print(buenasNoches())
else:
     print("Hora invalida")
