count = 0

for number in range(1,10):
    if number %2 == 0:
        count = count+1
        print(number)
print(f"We have {count} numbers")