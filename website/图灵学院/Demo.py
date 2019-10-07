class Person:
    name = ''
    age = 110

    def __init__(self,name,age):
        self.name = name
        self.age = age

one = Person('zhankeqing',25)
f = getattr(one,'name')
print(f)
