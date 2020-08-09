#import urllib
# log = open("logfile.txt","w")
# url="https://www.baidu.com"
# print("downloading file from url",url,file=log)
# text=urllib.urlopen(url).read()
# print("file successfully downloaded",file=log)
import logging
logging.basicConfig(level=logging.INFO,filename="mylog.log")
logging.info("Starting program")
logging.info("Trying to divide 1 by 0")
print(1/0)

logging.info("The division succeeded")
logging.info("Ending program")
