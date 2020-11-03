import random

#################################
## Animal abstract data type 
#################################
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self): # retorna el valor de la variable age
        return self.age
    def get_name(self): #retorna el nombre de la variable name
        return self.name
    def set_age(self, newage):#actualiza el valor de la variable age
        self.age = newage
    def set_name(self, newname=""):#actualiza el valor de la variable name
        self.name = newname
    def __str__(self):#pasa a cadena la edad y el nombre
        return "animal:"+str(self.name)+":"+str(self.age)
        
print("\n---- animal tests ----")
a = Animal(4)#declara un objeto de animal con edad igual a 4
print(a) #imprime el objeto y sus valores(nameClass, age, name)
print(a.get_age())#imprime el valor age del objeto
a.set_name("fluffy")# cambia el valor del nombre de none a fluffy
print(a)#imprime el objeto y sus valores(nameClass, age, name)
a.set_name()#actualiza el valor de la variable name, pero no es obligatorio pasar un valor porque tiene uno por omision
print(a)#imprime el objeto y sus valores(nameClass, age, name)



#################################
## Inheritance example 
#################################
class Cat(Animal):# clase hija de Animal
    def speak(self):#metodo propio de cat
        print("meow")
    def __str__(self):#pasa a cadena la edad y el nombre(modifica la de la super clase)
        return "cat:"+str(self.name)+":"+str(self.age)
    
print("\n---- cat tests ----")
c = Cat(5)#crea un objeto de cat
c.set_name("fluffy")#modifica la varible name, como la hereda entonces puede hacerlo
print(c)#imprime el objeto y sus valores(nameClass, age, name)
c.speak()#llamado a la funcion speak()
print(c.get_age())#imprime el valor de age
#a.speak() # error because there is no speak method for Animal class

    
#################################
## Inheritance example
#################################
class Person(Animal):#clase hija de animal
    def __init__(self, name, age):#constructor
        Animal.__init__(self, age)#constructor de la super clase(permire usar lo de la cuper clase)
        self.set_name(name)#cambia el estado de name(Animal)
        self.friends = []#lista
    def get_friends(self):#retrona el la lista
        return self.friends
    def speak(self):#imprime un mensaje(no es la misma de cat)
        print("hello")
    def add_friend(self, fname):#agrega a la lista
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):#evalua la diferencia de edad entre dos objetos
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):#pasa a cadena la edad y el nombre(modifica la de la super clase)
        return "person:"+str(self.name)+":"+str(self.age)

print("\n---- person tests ----")
p1 = Person("jack", 30)#crea un objeto
p2 = Person("jill", 25)#crea un objeto
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)
#La clase crea varios metodo propios de ella misma y tambien modifica algunos de la super clase, luego implementa cada uno de ellos


#################################
## Inheritance example
#################################
class Student(Person):#clase hija de persona
    def __init__(self, name, age, major=None):#Constructor
        Person.__init__(self, name, age)#contructor que permite usar lo de la super clase
        self.major = major#variable propia de Student
    def __str__(self):#actualiza el metodo de la superclase
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):#metodo propio que actualiza el valor de major
        self.major = major
    def speak(self):#actualizacion del metodo de la super clase
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1)
print(s2)
print(s1.get_name(),"says:", end=" ")
s1.speak()
print(s2.get_name(),"says:", end=" ")
s2.speak()

#la clase hereda los componentes de la clase Persona y autiliza sus atributos y algunos metodos modificados

#################################
## Use of class variables  
#################################
class Rabbit(Animal):#clase hija de Animal
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None): #Constructor con dos valores por omision y uno obligatotio
        Animal.__init__(self, age)#constructor de la super clase para usar los componentes de esta
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):#la funcio vulve la variable rid en un numero de n cifras colocando ceros a la izquierda del numero
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):#variable que retorna el valor de parent1
        return self.parent1
    def get_parent2(self):#variable que retorna el valor de parent1
        return self.parent2
    def __add__(self, other):#suma un pariente al objeto
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)

