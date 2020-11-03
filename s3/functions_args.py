def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario inválida')
        print(recordatorio)

pedir_confirmacion('¿Realmente queres salir?')
pedir_confirmacion('¿Sobreescribir archivo?', 2)
pedir_confirmacion('¿Sobreescribir archivo?', 2, "Vamos, solo si o no!")

# pedir_confirmacion(reintentos = 4, '¿Sobreescribir archivo?', "Vamos, solo si o no!")