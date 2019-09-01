def fn(a:int,b:bool,c:str='hello')->int:
	'''这是一个文档示例--函数 返回值 int   fn()->int
	函数参数：
	a:作用 类型 int 不是强制，主要用于说明int
	b:作用 类型 bool
	c:作用 类型 str 默认 hello
	'''
	return 10
print(fn.__doc__) #只输出说明的部分没有help函数的返回来的详细
#help(fn)
