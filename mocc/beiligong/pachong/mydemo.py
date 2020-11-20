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
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all("a")