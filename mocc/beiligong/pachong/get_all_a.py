from bs4 import BeautifulSoup
import requests
url = "http://python123.io/ws/demo.html"
r=requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

#print(soup.find_all("a"))
print(soup.find_all(["a","b"]))

for link in soup.find_all("a"):
    print(link.get("href"))
