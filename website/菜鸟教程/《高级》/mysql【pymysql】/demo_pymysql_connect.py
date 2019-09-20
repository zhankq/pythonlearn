#PyMySQL [连接]
##安装 mysql扩展
#$ pip3 install PyMySQL

import pymysql
#打开数据库连接
db = pymysql.connect("localhost","root","","runoob_db");
#使用cursor() 方法创建一个游标对象 cursor 
cursor = db.cursor()

#使用execute() 方法执行 SQL 查询
cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : {}".format(data));

db.close()