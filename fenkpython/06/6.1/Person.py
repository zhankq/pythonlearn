class Person:
    '这是一个学习Python定义的一个Person类'
    hair = "black"
    def __init__(self,name="Charlie",age=8):
        #定义实例变量
        self.name = name
        self.age = age
    #定义一个say() 方法
    def say(self,content):
        print(content)
# help(Person)
p = Person()
print(p.name,p.age)
p.name = "李刚"
p.say("Python语言很简单，学习很容易！")
print(p.name,p.age)
#为P对象增加一个skills实例变量
p.skills = ["programming","swimming"]
print(p.skills)
del p.name
#print(p.name)#AttributeError:
def info(self):
    print("-----info函数----",self)
#使用info对p的foo方法赋值（动态绑定方法）
p.foo = info
p.foo(p) #输出函数
# 使用lambda表达式为p对象的bar方法赋值（动态绑定方法）
p.bar = lambda self:print("--lambda表达式--",self)
p.bar(p)
def intro_func(self,content):
    print("我是一个人，信息为: %s" % content)
#导入MethodType
from types import MethodType
#使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为p
p.intro = MethodType(intro_func,p)
# 第一个参数已经绑定了，无需传入
p.intro('生活在别处')
