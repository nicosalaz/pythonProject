fib = [0,1]
def fibo(serie):
    contaX = 0
    contaY = 1
    for x in range(2,20):
        serie.append((serie[contaX]+serie[contaY]))
        contaX+=1
        contaY+=1
fibo(fib)

def es_primo(num):
    if num == 1 or num == 2:
        return num
    for x in range(2,num):
        if num % x == 0:
            return False
        else:
            return num

print('Serie Fibo: ',fib)
primos =list(filter(es_primo,fib))
print('Es primos: ',primos)