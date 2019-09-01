#from urllib.request import urlopen
import urllib.request
#webpage = urlopen("https://www.163.com")
#print(webpage.read())
urllib.request.urlretrieve("https://www.163.com",'a.txt')