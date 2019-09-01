#StopIteration
#StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
	"""docstring for MyNumbers"""
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <=6 :
			x=self.a
			self.a +=1 
			return x
		else:
			raise StopIteration
		
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)

'''
执行输出结果为：

1
2
3
4
5
6
'''

##把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
'''
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x=self.a
		self.a+=1
		return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
