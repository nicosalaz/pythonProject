def parent(num):
    def first_child():
        return "Hola, Yo soy Juan"

    def second_child():
        return "Llámame Ana"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first)
print(first())
print(second)
print(second())