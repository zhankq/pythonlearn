class Fruit:
	def info(self):
		print('我是一个水果！重 %g 克' % self.weight)

class Food:
	def taste(self):
		print("不同食物的口感不同")

class Apple(Fruit,Food):
	pass

#创建Apple对象
a = Apple()
a.weight = 5.6
#调用 Apple对象的info方法
a.info()
#调用 Apple 对象的taste() 方法
a.taste()