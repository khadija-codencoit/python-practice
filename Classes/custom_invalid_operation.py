# class InvalidOperationError(Exception):
#     pass

# class stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#        if self.opened :
#            raise IndentationError ("Stream is already opened")
       
#     def close(self):
#        if not self.opened :
#            raise IndentationError ("Stream is already closed")

# class NewtworkFileStream(stream):
#     def read(self):
#         print("Reading data from network")



# ======================================

# from abc import ABC , abstractmethod, ABCMeta

# class Animal(metaclass=ABCMeta):
#     def __init__(self):
#         self.name = ""
#         self.color = "" 

#     @abstractmethod
#     def sound(self):
#         pass

    
# class Dog(Animal):
#     def sound(self):
#         print("Dog Sound")

#     def callingSound(self):
#         print("Gheu Gheu")

# class Cat(Animal):
#     def sound(self):
#         print("Cat sound")

# jerman_shepar = Dog()
# jerman_shepar.callingSound()
# jerman_shepar.sound()

# cat = Cat()
# cat.sound()

# class Chiken(Animal):
#     def sound(self):
#         print("chiken sound")

#     def rong(self):
#         print("Browny")

# broylar = Chiken()
# broylar.sound()
# broylar.color()


##Problem 2
#Create an abstract base class Employee with:
# name (attribute)
# An abstract method: calculate_salary()
# Create two subclasses:
# FullTimeEmployee — gets a fixed monthly salary
# PartTimeEmployee — gets paid based on hourly rate × hours worked
# Each subclass must implement calculate_salary() method.

# Create and test at least one object of each type and print their salary.

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def calculatte_salary(self):
        pass
        
class FullTimeEmployee(Employee):
    def __init__(self, name,monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary


    def calculatte_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name,hourly_rate):
        super().__init__(name)
        self.hourly_rate = hourly_rate

    def calculatte_salary(self):
        return self.hourly_rate
        
khadija = FullTimeEmployee("khadija",1000000)
print(khadija.name,khadija.monthly_salary)