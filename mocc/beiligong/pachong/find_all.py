from bs4 import BeautifulSoup
import requests,re
url = "http://python123.io/ws/demo.html"
r=requests.get(url)
demo = r.text

#demo = "<a id='ss' rel='good' class='fff'>AAA</a>"

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

#for tag in soup.find_all(["p","a"],id="link1"):
# for tag in soup.find_all(id="link1"):
#      print(tag,'===')
#s = soup.find_all(["a"],'id')

print(soup.find_all("a"))

#print(s)