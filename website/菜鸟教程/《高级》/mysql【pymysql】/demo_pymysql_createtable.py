import pymysql
#打开数据库连接 【建表】
db = pymysql.connect("localhost","root","","runoob_db")

cursor = db.cursor()

cursor.execute("drop table if exists employee")

# 使用预处理语句创建表
sql = """CREATE TABLE employee (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
db.close()