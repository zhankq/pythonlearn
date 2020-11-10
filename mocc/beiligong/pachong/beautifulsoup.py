from bs4 import BeautifulSoup
import requests
url = "http://python123.io/ws/demo.html"
r=requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# print(soup.prettify())

tag_a = soup.a
tagname = soup.a.name

tagnameparent  = soup.a.parent.name
print(tagnameparent)

print(tag_a.attrs)
print(tag_a.string)
newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a commit</p>","html.parser")
print(type(newsoup.b.string))
print(newsoup.b.string)
print(newsoup.p.string)

print(soup.title.parent)
print(soup.parent)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
