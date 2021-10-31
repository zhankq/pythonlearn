class Record:
	#定义两个变量
	item = "鼠标"
	date = "2016-06-16"
	def info(self):
		print("info方法中：",self.item)
		print("info方法中：",self.date)

rc = Record()
print(rc.item)
print(rc.date)
rc.info()

#w修改Rcord类的两个变量
Record.item="键盘"
Record.date = "2021-08-24"

rc.info()
#print(rc.item)