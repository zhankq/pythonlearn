class Person:

    count=10


    def __init__(self,name,phone):
        self._name = name
        self.__phone = phone
    def say_hi(self):
        print('name')

    def get_phone(self):
        return self.__phone

    @property
    def name(self):
        print("get execute")
        return self._name

    #setter 方法的装饰器：@属性名.setter
    @name.setter
    def name(self,name):
        self._name = name

    #类方法
    #类方法的第一个参数 cls ，也会自动传递 ，cls就是当前的类对象
    #类方法与实例方法的区别，实例方法的第一个参数是self，类方法的第一个参数是cls
    #可以用实例方法也可以类方法的时候用。
    @classmethod
    def test_2(cls):
        print(cls.count)

    #静态方法
    #@staticmethod 来修饰的方法属于静态方法
    #静态方法与类无关的方法，她只是一个保存在当前 类中的函数
    #静太方法一般是一些工具方法，和当前类无关
    @staticmethod
    def test_3():
        print("test_3 执行了~~~~")

    def __del__(self):
        print("对象被删除了...")

    #def __str__(self):
     #   print('??')




one = Person('zhangsan','13868049744')
one2 = Person('zhangsan','13868049744')

f = getattr(one,'name')
print(f)


print(one2)

del one2
#one.say_hi();
print(one.__dict__)


print(one.test_3())

print(one.count)
print(Person.count);
Person.count = 110
print(one.count)




print(one.name)
one.name='1283'
print(one.name)


phones = one.get_phone();
print(phones)


one._Person__phone = '123'
phones = one.get_phone();
print(phones)


