class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point = Point(1,2)
other = Point(1,2)

print(point == other)

##practice 
#Problem -1
# 1. Create a Book class
# Attributes: title, author, price

# Method: __eq__ that returns True if two books have the same title and author.

class Book:
    def __init__(self,title,author,price):

        self.title = title
        self.author = author
        self.price = price

    def __eq__(self,book):
            return self.title == book.title and self.author == book.author


book = Book("Alchemist","khadija",999)       
other = Book("Alchemist","khadija",999)   
print(book)

# print(f"Title = {book.title} Author = {book.author}")
# print(f"Title = {other.title} Author = {other.author}")

# print(book == other)