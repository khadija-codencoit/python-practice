n = input()

def fizzbazz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return "fizzbazz"
    if n %3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    
print(fizzbazz(15))