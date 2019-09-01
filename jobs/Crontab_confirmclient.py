import pymysql
import  datetime
import time

''''
# 打开数据库连接
db = pymysql.connect("rm-wz9770f5797u7ra16233.mysql.rds.aliyuncs.com","kdt_yunfen","60xD9%v0LQfc@lFP","yunfenba" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
'''

day = datetime.datetime.today().date()


todaytime = int(time.mktime(time.strptime(str(day), '%Y-%m-%d')))

sql = "SELECT id,add_time,confirm_time FROM  wf_aduser WHERE confirm_time = %d and add_time>%d" % (0,todaytime)
print(sql)

