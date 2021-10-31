class Dog:
	__slots__ = ('walk','age','name')#只对实例起作用

	def __init__(self,names):
		self.name = names

	def test():
		print("预先定义的test方法")

d = Dog('Snoopy')

from types import MethodType
# 只允许动态为实例添加walk、age、name这3个属性或方法
d.walk = MethodType(lambda self:print("%s正在慢慢地走" % self.name),d)
d.age = 5

d.walk()
# d.foo = "aas"
Dog.foo = "saa"

print(d.foo)

Dog.bar = lambda self:print("abc")
d.bar()

class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass


gd = GunDog('Puppy') #__slots__对子类没有影响
# gd = GunDog("Puppy")
gd.speed  =99

print(gd.speed)