class ItemMetaClass(type):
	def __new__(cls,name,bases,attrs):
		#动态类添加一个cal_price方法
		attrs['cal_price'] = lambda self:self.price * self.discount
		return type.__new__(cls,name,bases,attrs)

#利用metaclass批量生成一批带特征的类
#定义book类
class Book(metaclass=ItemMetaClass):
	__slots__ = ('name','price','_discount')
	def __init__(self,name,price):
		self.name = name
		self.price = price

	@property
	def discount(self):
		return self._discount

	@discount.setter
	def discount(self,discount):
		self._discount = discount
#定义cellphone类
class CellPhone(metaclass=ItemMetaClass):
	__slots__ = ('price','_discount')

	def __init__(self,price):
		self.price = price

	@property
	def discount(self):
		return self._discount
	
	@discount.setter
	def discount(self,discount):
		self._discount = discount

#此处,cp与b对象是同源，所以可以相互使用
b = Book('疯狂python讲义',89)
b.discount = 0.76
print(b.cal_price())
cp = CellPhone(2399)

cp.discount = 0.85

print(cp.cal_price())