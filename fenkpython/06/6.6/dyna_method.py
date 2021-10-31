class Cat:
	
	def __init__(self,name):
		self.name = name

#这个定义本身是为类使用的,且是为类当中有name属性才可用
def walk_func(self):
	print("{}慢慢地走过一片草地".format(self.name))


d1 = Cat("Garfield")
d2 = Cat("Kitty")

#为类赋属性
Cat.walk = walk_func
Cat.params = "good job"#添加属性

#这挺神奇的，定义后的类实例，还能使用类之后 生成的动态方法与变量
d1.walk()
d2.walk()

print(d1.params)




s = {'name':"good"}

print(s['name'])

def struct():
	pass

o = struct()
#o.name = "good" #error
#walk_func(o)