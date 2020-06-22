class person:
	#def __new__(cls):
	#	print("----")

	def __init__(self,age):
		_age = age
		print("ffffffff")

	def __str__(self):
		return "hello __str__"

		#两个对象间的比较
	def __gt__(self,other):
		return self.age>other.age



s = person()
print(s)