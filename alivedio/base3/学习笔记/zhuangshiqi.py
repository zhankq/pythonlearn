def add(a,b):
    '''
求任意两个数的和
'''
    r = a + b
    return r

def mul(a,b):
    '''求任意两个数的积
'''
    r = a * b
    return r

def fn():
    print("我是fn函数...")

def fn2():
    print("函数开始执行~~~")
    fn()
    print("函数执行结束~~~")


def new_add(a,b):
    print("计算开始~~~")
    r = add(a,b)
    print("计算结束~~~")
    return r

#res = new_add(2,5)
#print(res)

def begin_end(old):

    def new_function(*args,**kwargs):
        print("开始执行~~~")
        result = old(*args,**kwargs)
        print("执行结束~~~")
        return result

    return new_function

'''
#f = begin_end(fn)
f2 = begin_end(add)
s = f2(2,3)
print(s)
'''
def fn3(old):

    def new_function(*args,**kwargs):
        print('fn3装饰~开始执行~~~~')
        res = old(*args,**kwargs)
        print('fn3装饰~执行结束~~~~')
        return res

    return new_function

'''
@fn3
@begin_end
def say_hello():
    print('大家好~~~')

say_hello()
'''

s = add(1,2)
print(s)
