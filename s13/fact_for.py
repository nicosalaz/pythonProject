import time

def fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

start_time = time.time()

print (fact(5000))

print("--- %s seconds ---" % (time.time() - start_time))
