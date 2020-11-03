def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("El factorial de ", num, "es", factorial(num))