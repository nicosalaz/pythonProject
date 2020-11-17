import time

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

start_time = time.time()

print (fact(250000))

print("--- %s seconds ---" % (time.time() - start_time))
