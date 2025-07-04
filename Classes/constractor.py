## Problem 1
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {(self.x),(self.y)}")

point = Point(5,6)
point.draw()

## Problem 2
#Create a class Car with attributes brand, model, and year. Add a method to display car details

class Car():

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f" Car {self.brand} {self.model} {self.year}")
        
my_car = Car("Toyota", "Corolla", 2022)
my_car.display()


##Problem 3
# Create a class Movie with attributes:

# title
# director
# year
# Use a constructor to initialize the values. Add a method display() to print the movie info.
# Create two Movie objects and display their info.

class Movie:
    def __init__(self,title,director,year):
        self.title =title
        self.director = director
        self.year = year

    def display(self):
        print(f"Movie Information {self.title} {self.director} {self.year}")

movie = Movie("Titanic","khadija",1990)
movie.display()

##Problem 4
# Create a class Rectangle with attributes length and width, initialized using the constructor.
# Add a method get_area() that returns the area of the rectangle.
# Create two rectangle objects and print their areas.


class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def get_area(self):
        area = self.lenght * self.width
        print(f"Area is {area}")
        
rectangle1 = Rectangle(4,5)
rectangle2 = Rectangle(8,7)
rectangle1.get_area()
rectangle2.get_area()

## Problem 5
class Record:
    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")

    def calculate_year_of_birth(self):
        year_of_brith = 2025 - self.age
        print(f"Year of Birth: {year_of_brith}")



person = Record("Khadija", "khatun", 16)
person.calculate_year_of_birth()
# dob =fahmid.calculate_year_of_birth()
# print(f"Year of Birth: {fahmid.calculate_year_of_birth()}")


khadija = Record("khadija", "Khatun", 26)
dob = khadija.calculate_year_of_birth()



class Student(Record):
    def __init__(self, f_name, l_name, age, student_id):
        super().__init__(f_name, l_name, age)
        self.student_id = student_id
        print(f"Student ID: {self.student_id}")

    def calculate_year_of_birth(self):
        print("Calculate birth year.")



halima = Record("Halima", "Khatun", 25)
#halima = Student("Halima", "Khatun", 25, "S12345")
halima.calculate_year_of_birth()


## Problem 6
# Create a class BankAccount with attributes account_number and balance.
# In the constructor, make sure the balance cannot be negative.
# Raise an exception or print an error message if it is.

class BankAccount:
    def __init__(self,account_number,balance):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.account_number = account_number
        self.balance = balance

    def show(self):
        print(f"Account Number {self.account_number}")
        print(f"Blance {self.balance}")

bankaccount = BankAccount(543,999)      
bankaccount.show()








        