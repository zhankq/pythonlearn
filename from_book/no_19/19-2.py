from configparser import ConfigParser
from s import JOB
#import s
print(JOB)

CONFIGFILE = "area.ini"

config = ConfigParser()
#读取配置文件
config.read(CONFIGFILE)
#打印默认问候语（greeting）
#在messages部分查找 问候语
print(config['messages'].get("greeting"))
#使用配置文件中的提示 （question）让用户输入半径
radius = float(input(config["messages"].get("question")+' '))

print(config["messages"].get("result_message"),end=" ")


print(config["numbers"].getfloat('pi')*radius**2)
