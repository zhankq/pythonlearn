from bs4 import BeautifulSoup
import requests,re
url = "http://python123.io/ws/demo.html"
r=requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(demo)
#获取所有的标签名
# for tag in soup.find_all(True):
#     print(tag.name)
# print("---------------------------")
#获取所有的标签名中对包含指定字符串的标签
# for tag in soup.find_all(re.compile("b")):
#     print(tag.name)
#<>.find_all(name, attrs, recursive, string, **kwargs)

for tag in soup.find_all(["p"],"course"):
    print(tag.string)
