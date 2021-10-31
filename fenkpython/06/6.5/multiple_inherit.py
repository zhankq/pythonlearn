class Item:
	def info(self):
		print("Item中方法:","这是一个商品")

class Product(object):
	"""docstring for Product"""
	def info(self):
		print("product中方法:","这是一个工业产品")

class Mouse(Item,Product):
	pass

#静下来看书是很好的体验
m=Mouse()
#Item的info方法覆盖了Product的
m.info()