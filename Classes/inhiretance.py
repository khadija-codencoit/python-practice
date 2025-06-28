class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

#Animal = parent,Base
#Mammal = child,sub

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()

##Problem-1
# Create a base class Vehicle with a method start(). 
# Create a subclass Car that inherits from Vehicle and adds a method drive().
# Then create an object of Car and call both methods.

class Vehicle():
    def start(self):
        print("Verical is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is moving")

m = Car()
m.start()
m.drive()