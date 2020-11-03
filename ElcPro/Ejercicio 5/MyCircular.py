class Mycircular():
    def __init__(self, *letras):
        self.letras = letras
        self.index = 0
        self.retroceso = False
    def __iter__(self):
        return self

    def __next__(self):
        value = ""
        if self. index <= -1:
            raise StopIteration
        elif self.retroceso == False:
            value = self.letras[self.index]
            self.index += 1
            if self.index == len(self.letras):
                self.retroceso = True
                self.index = len(self.letras)-2
        elif self.retroceso == True:
            value = self.letras[self.index]
            self.index-=1
        return value

for letter in Mycircular(['a','b','c']):
    print(letter)