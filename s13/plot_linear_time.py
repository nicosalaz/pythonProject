import matplotlib.pyplot as plt
import time

def linear_algo(n):
    for value in range(0,n):
        pass

start_time = time.time()

x = [2000, 8000, 14000, 20000, 26000]

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
plt.title('Lineal Complexity')
plt.show()



