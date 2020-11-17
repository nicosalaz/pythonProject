import time

def constant_algo(items):
    result = items[0] * items[0]
    return result

start_time = time.time()

x = constant_algo([4, 5, 6, 8])

print(x)

print("--- %s seconds ---" % (time.time() - start_time))
