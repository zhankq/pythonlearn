class Bird:
	#classmethod修饰的方法是类方法
	@classmethod
	def fly(cls):
		print("类方法fly:",cls)
	#staticmethod修饰的方法是静态方法
	@staticmethod
	def info(p):
		print("静态方法info:",p)

#调用 类方法，Bird类会自动绑定到第一个参数 
Bird.fly()
# 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info("crazyit")
# 创建Bird对象
b = Bird()
b.fly()

b.info("fkit")

