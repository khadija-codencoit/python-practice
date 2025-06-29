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