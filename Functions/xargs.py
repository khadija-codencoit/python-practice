def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(7,8,9))