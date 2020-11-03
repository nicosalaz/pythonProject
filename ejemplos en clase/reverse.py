class MyEnumerate():
    def __init__(self, data):
        self.data = data
        self.index = len(data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = (self.index, self.data[len(self.data)-(self.index+1)])
        self.index -= 1
        return value

for index, letter in MyEnumerate('abc'):
    print(f"{index} : {letter}")
