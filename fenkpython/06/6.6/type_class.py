def fn(self):
	print('fn函数')

#使用type()定义Dog类
Dog = type('Dog',(object,),dict(walk=fn,age=6))
# Dog = type('Dog',(object,),dict(walk=lambda self: "aaaaaaa",age=6))
#创建了Dog对象，继承自object,方法walk,成员变量age

d = Dog()

print(type(d))  
print(type(Dog))
d.walk()
print(Dog.age)
