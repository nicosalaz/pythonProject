def vowels():
    yield "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"

for i in vowels():
    print(i)


def vowels():
    return "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"

for i in vowels():
        print(i)