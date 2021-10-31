class Employee:
	def __init(self,salary):
		self.salary = salary
	def work(self):
		print("普通员工正在写代码,工资是:",self.salary)

class Customer:
	def __init__(self,favorite,address):
		self.favorite = favorite
		self.address = address

	def info(self):
		print("我是一个顾客,我的爱好是:%s,地址是%s" % (self.favorite,self.address))

class Employee2:
	def __init__(self,favorite,address):
		self.address = address
		self.favorite = favorite
		
	def work(self):
		print("普通员工正在写代码,工资是:",self.address)


#Manager继承了Employee,Customer
# class Manager(Employee,Customer):
class Manager(Employee2,Customer):#如果都是两个参数且参数名是一样的则不受影响
	pass

m = Manager("IT产品","广州")
m.work()
m.info()		