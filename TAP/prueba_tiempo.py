import time
def cronometro(limite):
    actual = limite
    est = False
    for min in range(0,60):
        if min == limite:
            est = True
            break
        elif min < limite:
            actual = limite-min
        print('quedan:',actual,'minutos')
        for sec in range(0,60):
            time.sleep(1)
        return est

cronometro(1)