number = 10

while number>0:
    print(number)
    number //=2


###
commend = ""
while commend.lower() != "quit":
    commend = input(">")
    print("ECHO",commend)

##Another way

while True:
    commend = input(">")
    print("ECHO",commend)
    if commend.lower() == "quit":
        break
   