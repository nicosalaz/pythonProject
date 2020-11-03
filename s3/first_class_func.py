def say_hello(name):
    return f"Hola {name}"

def be_awesome(name):
    return f"{name}, juntos somos sorprendentes!"

def greet_bob(greeter_func):
    return greeter_func("Ana")

print(say_hello("Fernando"))
print(be_awesome("Fernando"))
print(greet_bob(say_hello))
print(greet_bob(be_awesome))