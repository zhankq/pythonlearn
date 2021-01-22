import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url,code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL,"gbk")
    strs = re.findall(r'<div class=\"news_item\">.*?</h3>',html,re.DOTALL)
    for i in strs:
        m=re.search(r'<a href="(.*?)">(.*?)</a>',i)
        lst.append([m.group(1),m.group(2)])


lst = []
url = 'https://sports.163.com/dj/'
s = getStockList(lst,url)
# print(lst)
html = getHTMLText(url,'gbk')
soup = BeautifulSoup(html, 'html.parser')

print(soup.title.text)

stockInfo = soup.find_all('div',attrs={'class':'news_item'})
#print(stockInfo)
lst = []
for info in stockInfo:
   # print(info.h3)
   lst.append([info.h3,info.h3.string])
   # print(info.a.attrs['href'])
    # print(type(info))
    # print(info.prettify())
    #m=re.search(r'<h3>.*?<a href="(.*?)">(.*?)</a></h3>',info.prettify(),re.DOTALL)
    # print(m.group(0))
    # print(m.group(2))

print(lst)
