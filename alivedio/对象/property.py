class Person:
	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		print("set name")
		self._name = name

p=Person("fff")

p.name="ffffff"



	