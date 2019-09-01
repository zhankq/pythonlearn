'''
a=179
scope = locals() #当前命名空间内

#print(scope)

#print(scope['a'])

scope['ac'] = 99

#print(ac)  #输出：99  -->别这样用

def asf():
    global a
    f=globals()
    print(f['ac'])
    print(f['a'])
    print(f['jobs'])

jobs = 991
asf()
'''

def a():
    f='123'
    def s():
        nonlocal f
        print(f)
        f='fffff'
    s()
    print(f)

a()
