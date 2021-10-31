#在子类中调用 父类
class BaseClass:
	def foo(self):
		print("父类中定义的foo方法")

class SubClass(BaseClass):
	#重写父类的foo方法
	def foo(self):
		print('子类中重写父类中的foo方法')

	def bar(self):
		print("执行bar方法")
		self.foo()
		BaseClass.foo(self)

sc = SubClass()
sc.bar()