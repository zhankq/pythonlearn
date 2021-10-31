class Role:
	pass

r = Role()
#查看变量r的类型
print(type(r)) #<class '__main__.Role'>
#说明 定义 类本身即可视为一个 type类的对象
print(type(Role)) #<class 'type'>