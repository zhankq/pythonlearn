def fn4(a,b,c,d):
    print(a,b,c,d)

t=(1,2,3,4)
fn4(*t)
t2 = {'a':21,'b':32,'c':12,'d':32}
fn4(**t2)

def f3(a,b,*,c):
    return a+b+c


f3(1,2,c=3)
'''
def fn4(a,b,c,d):
    print(a,b,c,d)

 t=(1,2,3,4)
 fn4(*t)
'''
