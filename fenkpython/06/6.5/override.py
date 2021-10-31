#关于类方法重写的布局
class Bird:
	def fly(self):
		print("飞飞...")

class Ostrich(Bird):
	#重写fly()方法
	def fly(self):
		print("我只能在地上奔跑...")

os = Ostrich()
os.fly()