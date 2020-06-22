class Animal:

	def __init__(self,whois):
		self._whois = whois


	def sleep(self):
		print("sleep....")

	def run(self):
		print("run....")

class Dog(Animal):
	"""docstring for Dog"Anima"""

	'''
	def __init__(self, arg):
		super(Dog,Animal).__init__()
		self.arg = arg
	'''

	def __init__(self,name,whois):
		super().__init__(whois)
		self._name = name


	def whois(self):
		print(self._whois)

	def bark(self):
		print("wang wang ...")

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name = name
		
	

d = Dog("旺财","vancekq")
#d.run()
#d.bark()
d.whois()

#print(issubclass(Dog,Animal))