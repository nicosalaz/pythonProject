def my_decorator(func):
    def wrapper():
        func()
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    return True
@my_decorator
def say_hello():
    print("Hello!")

print(say_whee())