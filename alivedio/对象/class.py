class MyClass():
    pass

mc = MyClass()

print(type(mc))

mc.name="jobs"

print(mc.name)

def ass(a:int,b:str)->int:
    return a+int(b)


val = ass(23,"123")
print(val)


class MyClass2():
    a=10
    b=20

p1 = MyClass2()
p1.a
