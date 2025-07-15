import random
import string


# print(random.random())
# print(random.randint(1,10))
# print(random.choices([2,88,9,7,6],k=2))
# print("".join(random.choices("kjgfdsasdfg",k=2)))
# print("".join(random.choices(string.ascii_letters + string.digits,k=5)))

# print(string.ascii_uppercase)

###Practice
# Random Password Generator

# Write a program that generates a random password of length 8 using:
# uppercase
# lowercase
# digits
# special characters (!@#$%^&*())

combain = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(!@#$%^&*())"
password = "".join(random.choices(combain , k=8))

print("Generated Password:",password)

#Problem -2
# OTP Generator
# Create a function generate_otp() that returns a random 6-digit number as a string.

def generate_otp():
    return "".join(random.choices(string.digits,k=4))


otp = generate_otp()
print(otp)

#prolem 3
# Random Name Selector
# Given a list of names, randomly select one person to win a prize.

name_list = ['khadija','halima','ibrahim',"kk"]

print((random.choice(name_list)))

##Problem-4
# Random Sentence Creator

# Write a function that randomly builds a sentence using three lists:

# subjects: ["I", "You", "We"]
# verbs: ["like", "hate", "see"]
# objects: ["pizza", "movies", "coding"]

def make_sentance():
    subjects =  ['I', "You", "We"]
    verbs = ["like", "hate", "see"]
    objects =["pizza", "movies", "coding"]


    # print("Random Santance"," ".join(random.choices(com,k=3)))
    print("Random Santance",random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects))

make_sentance()

