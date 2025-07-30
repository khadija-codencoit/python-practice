import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")
#print(soup.prettify())
# soup.find_all("a")
print()

content = soup.find_all("body",attrs={
   "class": "questions-page unified-theme"
})
print(content)



# ancohor = soup.find_all("a")
# #print(ancohor)

# all_link = set()

# for a in ancohor:
    
#     link = a.get("href")
#     all_link.add(link)
#     print(link)