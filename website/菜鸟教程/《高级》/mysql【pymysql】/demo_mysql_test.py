import mysql.connector

##安装 mysql扩展
##python -m pip install mysql-connector

'''
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE runoob_db")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
			
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="runoob_db"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
#mycursor.execute("CREATE table sites(name VARCHAR(255),url VARCHAR (255))")
#mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
 
mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")
'''
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
 
mycursor.executemany(sql, val)
mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
#print(mycursor.rowcount, "记录插入成功。")

'''

##获取最后一条的插入纪录
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)

mydb.commit()  
print("1 条记录已插入, ID:", mycursor.lastrowid)
'''

##获取全部的数据
'''
mycursor.execute("SELECT id,name,url FROM sites limit 1,2")
 
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
 
for x in myresult:
  print(x)
  '''

#如果我们只想读取一条数据，可以使用 fetchone() 方法：
'''
mycursor.execute("SELECT name,url from sites where id=2");
myresult=mycursor.fetchone()

print(myresult)
'''
#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
'''
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB", )
mycursor.execute(sql, na)
myresult = mycursor.fetchall() 
for x in myresult:
	print(x)
'''





