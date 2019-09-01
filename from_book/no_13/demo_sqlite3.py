import sqlite3

conn = sqlite3.connect("food.db")
curs = conn.cursor()

#创建表
#curs.execute(
'''
create table food(
desc text,
water float,
kcal float,
protein float
)
'''
#)


#插入数据记录

query = "insert into food values(?,?,?,?)"
s=curs.execute(query,['hi,guys',12.3,12.4,54.1])
print(s)



sql = "INSERT INTO food(desc,water,kcal,protein) VALUES ('{}', {},  {},  {})".format ('Mac2', 3.1, 21, 240)
curs.execute(sql)

conn.commit()
print(sql)


'''
print(sql)
curs.execute(sql)
results = curs.fetchone()
print(results)
'''
try:
	curs.execute("select * from food")
	results = curs.fetchall()
	for row in results:
		print(row)
except:
	print ("Error: unable to fetch data")


conn.close()
