import webbrowser
import time

# print("welcome")
# webbrowser.open("http://facebook.com")



# problem-1
# Add a delay between opening each website.

# Use time.sleep() to wait 2 seconds between opening each site.

webbrowser.open("http://google.com")
time.sleep(10)
webbrowser.open("http://youtube.com")

# problem -2
# Give the user a menu to choose from (e.g., 1. Facebook, 2. Twitter, 3. Google), and open the selected site.

socile_median = ['facebook','youtube']

for index  , i in enumerate(socile_median,start=1):
    print(f"{index} {i}")

choice = input("Give your choice 1,2 : ")

if choice == 1:
    webbrowser.open("http://facebook.com")
else:
    webbrowser.open("http://youtube.com")