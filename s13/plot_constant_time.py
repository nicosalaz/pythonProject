import matplotlib.pyplot as plt
import time

def constant_algo(items):
    result = items[0] * items[0]
    return result

x = [2, 4, 6, 8, 10, 12]

y = list()

for i in x:
    start_time = time.time()

    x_value = constant_algo(x)

    y_value = time.time() - start_time

    y.append(y_value)

    print("--- %s seconds ---" % (y_value))

#plt.ylim(-1,1)

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()