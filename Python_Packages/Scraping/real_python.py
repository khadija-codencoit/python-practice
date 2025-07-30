import requests
from bs4 import BeautifulSoup
import csv



## Problem-1 :Get all link from Real Python website
url = "https://realpython.com/"
response = requests.get(url)

# print(htmlcontent)

soup = BeautifulSoup(response.content,"html.parser")
#print(soup.prettify())

# title = soup.title
# print(title)
all_links = set()

anchor = soup.find_all("div",attrs={
    'class' :"d-flex justify-content-center small mt-4"
})


for a in anchor:
    print("Newline = ",a)

    link = "https://realpython.com"+ a.get("href")
    if link:
        #all_links.add(link)
        print(link)


with open("link.csv",'w',newline='') as file:
    writer = csv.writer(file)
    for link in all_links:
        writer.writerow([link])