# def print_hello():
#     print("khadija")


# print_hello()
# def sum_cal(a,b):
#     return a+b

# sum =sum_cal(4,6)
# print(sum)


# def avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)

# avg(8,9,6)

#problem -1

county = ["Bangladesh","India","America"]

def country_len(county9):
    print(len(county9))

country_len(county)

#1. Greeting Function
#Write a function greet(name) that takes a name as input and prints:

def greet(name):
    print(name)

greet_name = "Khadija"
print(greet_name)

##2. Even or Odd
#Write a function is_even(num) that returns True if the number is even, otherwise False.

def is_even(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

number = is_even(9)
print(number)

#Find Maximum
#Write a function max_of_three(a, b, c) that returns the largest of three numbers.

def max_of_three(a,b,c):
    if a>b and a>c:
        print("A is max value")
    elif b>a and b>c:
        print("B is max value")
    else:
        print("C is max value")

max_value = max_of_three(9,8000,700000)
print(max_value) 

#4. Factorial
#Write a function factorial(n) using recursion that returns the factorial of a number.

def factorial(n):
    if n == 0 or n == 1: # This is base class.Recursion must always have a base case to stop. Otherwise, it will call itself forever and crash (infinite loop).
        return 1
    else:
       return n * factorial(n-1)

fac = factorial(7)
print(fac)

#5. Simple Calculator
#Write a function calculator(a, b, operator) that supports +, -, *, and /.

def calculator(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    else:
        operator == "/"
        return a/b



cal = calculator(4,9, "/")
print(cal)

# Count Vowels in a String
# Write a function count_vowels(s) that counts and returns the number of vowels in the string.


