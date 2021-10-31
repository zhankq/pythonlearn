import sys

a  = []
print(sys.getrefcount(a))
b = a

print(sys.getrefcount(a))

c= b
d=b
e=c
f =e
g=d
print(sys.getrefcount(a))



'''
a= []
# 两次引用，一次来自 a，一次来自 getrefcount

print(sys.getrefcount(a))

def func(a):
    ## 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a))

func(a)

print(sys.getrefcount(a))
'''