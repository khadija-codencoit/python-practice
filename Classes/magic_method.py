#Customizing Object Creation and Initialization

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} and {self.age}")


person = Person("kk",16)
person.display()



# Problem:

# Create a class Temperature that represents a temperature in Celsius. Implement the following magic methods:

# ✅ Requirements:
# __init__(self, celsius)

# Initializes the temperature.

# __str__(self)

# Returns a string like: "25°C"

# __eq__(self, other)

# Returns True if two temperatures are equal in Celsius.

class Teamperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def __str__(self):
        print(f"{self.celsius}" "25c")

    def __eq__(self, value):
        return self.celsius = value