'''
#改变了greet的行为，其实如果你把变量名换别的，greet就不会变了。
def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper

def greet():
    print("hello world")

greet = my_decorator(greet)
greet()
'''

'''
#装饰器实现类似功能
#装饰器可以理解成对原函数的扩展
def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper

@my_decorator
def greet():
    print("hello world")

greet()
'''

'''
#装饰器带个参数
def my_decorator(func):
    def wrapper(msg):
        print("wrapper of decorator")
        func(msg)
    return wrapper

@my_decorator
def greet(msg):
    print("hello world {}".format(msg))

greet('张三')
'''


'''
多个参数时用户 
#*arg,**kwargs
def tmp(*arg):
    print(arg)

def tmp2(**arg):
    print(arg)

tmp('a',"b")
tmp2(a=3)#针对位置变量
print({'a':"b"})
'''
'''
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("wrapper of decorator")
        func(*args,**kwargs)
    return wrapper

@my_decorator
def greet(i,j):
    print("res: {:d}".format(i+j))

res = greet(1,9)

def repeat(num):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(num):
                print("wrapper of decorator")
                func(*args,**kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)

greet("hello world")

print(greet.__name__) #wrapper
'''

'''
#保留原函数信息
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("wrapper of decorator")
        func(*args,**kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)

print(greet.__name__)
'''

'''
class Count:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self,*args,**kwargs):
        self.num_calls +=1
        print("num of calls is: {}".format(self.num_calls))
        return self.func(*args,**kwargs)

@Count
def example():
    print("hello world")

def my_decorator(func):
    def wrapper(msg):
        print("wrapper of decorator")
        func(msg)
    return wrapper

def my_decorator2(func):
    def wrapper(msg):
        print("wrapper of decorator2")
        func(msg)
    return wrapper 

#支持匹配多个装饰器
@Count
@my_decorator
@my_decorator2
def greets(msg):
    print("tmps"+msg)

# example()

greets("---")
'''



import functools
def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('execute decorator1')
        func(*args,**kwargs)
    return wrapper

def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('execute decorator2')
        func(*args,**kwargs)
    return wrapper

@my_decorator1
@my_decorator2
def greet(message):
    print(message)

greet('hello world')


####函数回顾-------------------------------------------------------------
'''
#函数做为变量
def func(message):
    print("Got g message:{}".format(message))

send_message = func

send_message('hello world')
'''

'''
#将函数做为变量传入另一个函数中
def get_message(message):
    return 'Got a message: '+message

def root_call(func,message):
    print(func(message))

root_call(get_message,"hello world")
'''

'''
#函数中定义新函数
def func(message):
    def get_message(message):
        print("Got message:{}".format(message))
    return get_message(message)

func('hello world')
'''

'''
#函数的返回值 以为函数返回
def func_closure():
    def get_message(message,dd):
        print("Got a message: {}".format(message))
        print(dd)
    return get_message

send_message = func_closure()
send_message("ddd","sss")
'''