import pymysql
db = pymysql.connect("localhost","root","","runoob_db")

cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > {}" .format(1000)

try:
	cursor.execute(sql)
#获取所有的记录
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
	print ("Error: unable to fetch data")

db.close()

