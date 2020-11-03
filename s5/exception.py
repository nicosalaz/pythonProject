while True:
    try:
        x = int(input("Digite un número: "))
        print("Usted ingresó " + str(x))
        break
    #except ValueError:\
        #print("Oops!  Ingresó un número inválido.  Intentelo de nuevo...")
    except:
        print("Error inesperado")