def primosFib(numero):
    result = []
    a, b = 0, 1
    while a < numero:
        if esPrimo(a) == True:
            result.append(a)
        a, b = b, a+b
    return result

def esPrimo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if x % n == 0:
                return False
        return True

print(primosFib(100))


