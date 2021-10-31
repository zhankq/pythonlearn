def funA(fn):
	print("A")
	fn()#执行传入的fn参数
	return "fkit"
'''
下面装饰效果相当于：funA(funB)，
funB将会替换（装饰）成该语句的返回值；
由于funA()函数返回fkit，因此funB就是fkit
'''
@funA
def funB():
	print("B")

print(funB)

def foo(fn):
	#定义一个嵌套函数
	def bar(*args):
		print("===1===",args)
		n = args[0]
		print("===2===",n*(n-1))
		#查看传给foo函数的fn函数
		print(fn.__name__)
		fn(n*(n-1))
		print("*"*15)
		return fn(n*(n-1))
	return bar

@foo
def my_test(a):
	print("==my_test==函数==",a)

# 打印my_test函数，将看到实际上是bar函数
print(my_test)

my_test(10)

my_test(6,5)

def auth(fn):
	def auth_fn(*args):
		#用一条语句执行模拟执行权限检查
		print("---模拟----权限检查")
		fn(*args)
	return auth_fn
@auth
def test(a,b):
	print("执行 test 函数,参数a:%s,参数b:%s" % (a,b))

test(20,50)