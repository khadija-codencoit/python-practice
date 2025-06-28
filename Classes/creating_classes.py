# Problem 1
class Point():
    first_name = "fahmid"
    last_name = ""

kk = Point()
kk.first_name = "khadija"
print(kk.first_name)
print(kk.last_name)

class Persone():
    name = "khadija Khatun"
    occupation = "Software Engineer"

person = Persone()
print(person.name,person.occupation)

##Problem 2
#Define a class named Student that holds student name, ID, and grade.
# Include a method to display student information.

class Student():
    name = ""
    id = ""
    grade = ""

    def info(self):
        print(f"{self.name} her id number is{self.id} and her grade is {self.grade}")

student = Student()
student.name = "khadija"
student.id = 123
student.grade = 4.00

student.info()