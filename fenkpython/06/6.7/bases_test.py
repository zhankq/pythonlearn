class A:
	pass
class B:
	pass
class D:
	pass

class C(A, B):
	pass

print("类A的所有父类:", A.__bases__)
print('类B的所有父类:', B.__bases__)
print('类C的所有父类:', C.__bases__) #(<class '__main__.A'>, <class '__main__.B'>)

print('类A的所有子类:',A.__subclasses__()) #都是类C

print('类B的所有子类:',B.__subclasses__())#都是类C