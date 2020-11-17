import time
import matplotlib.pyplot as plt

def linear_algo(n):
    for value in range(0,n):
        for value2 in range(0,n):
            pass

start_time = time.time()

x = [200, 800, 1400, 2000, 2600]

y = list()

for i in x:
    start_time = time.time()

    x_value = linear_algo(i)

    y_value = time.time() - start_time

    y.append(y_value)

    #print("--- %s seconds ---" % (y_value))

#plt.ylim(-1,1)

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Quadratic Complexity')
plt.show()