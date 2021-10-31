class User:
	def __hide(self):
		print("示范隐藏的hide方法")

	def getname(self):
		return self.__name

	def setname(self,name):
		if len(name)<3 or len(name)>8:
			raise ValueError('用户名长度必须在3～8之间')
		self.__name = name
	name = property(getname,setname)

	def setage(self,age):
		if age<18 or age>70:
			raise ValueError('用户名年龄必须在18在70之间')
			self.__age = age

	def getage(self):
		return self.__age

	def mymethod(self):
		return self.__hide()


#	age = property(getage,setage)

#创建User对象
u = User()
#对name属性赋值，实际调用 的setname 因为property函数定义了
#u.name = 'fk'
u.name = "fkit"
#u.age = 4
u.age = 19
#调用 getname
print(u.name)
#调用 getage
print(u.age)

# 尝试调用隐藏的__hide()方法
#类似直接调用 私有变量
#u.__hide()
#用类似的在类里面来调用 就可以了
u.mymethod()
#其实python并没有真正实现隐藏还有是办法绕过的
'''
#-----------不建议这么做-----
u._User__hide()
# 对隐藏的__name属性赋值
u._User__name = 'fk'
# 访问User对象的name属性（实际上访问__name实例变量）
print(u.name)
#-----------不建议这么做-----
'''