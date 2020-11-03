def my_decorator(func):
    def wrapper():
        print("Algo pasa antes que la función sea llamada.")
        func()
        print("Algo pasa después de que la función es llamada.")
    return wrapper

def say_whee():
    print("Whee!")
    return True

print(say_whee())
say_whee2 = my_decorator(say_whee)
print(say_whee2())