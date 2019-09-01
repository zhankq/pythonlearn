请注意，即使是整数也会被视为对象
字段有两种类型——它们属于某一类的各个实例或对象，或是从属于某一类本身。它们被分别称作实例变量（Instance Variables）与类变量（Class Variables）

#self 变量使用

Python 中的 self 相当于 C++ 中的 this 指针以及 Java 与 C# 中的 this 引用。
方法
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()

__init__ 方法
__init__ 方法会在类的对象被实例化（Instantiated）时立即运行

class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("Hello , my name is",self.name)

p = Person("Swaroop")
p.say_hi()

