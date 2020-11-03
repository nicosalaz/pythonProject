class LoudIterator():
    def __init__(self, data):
        print("Ejecutando __init__")
        self.data = data
        self.index = 0

    def __iter__(self):
        print("Ejecutando __iter__")
        return self

    def __next__(self):
        print("Ejecutando __next__")
        if self.index >= len(self.data):
            print(self.index, "y fin de los datos")
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        print(value, self.index)
        return value


for one_item in LoudIterator('abc'):
    print("dentro del ciclo ", one_item)