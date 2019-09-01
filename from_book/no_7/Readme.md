class 定义类时的代码都在一个特殊的命名空间【类的命名空间】内执行
而类的所有成员都可访问这个命名空间。

issubclass(son,parent) 判断 一个 两个类的关系【子类，父类】

超类
class Caolei:
    def cal(self,expression):
        self.value=eval(expression)

class Talker:
    def talk(self):
        print('hell',self.value)

class totals(Caolei,Talker):
    pass

f = totals()
f.cal('1+2')
f.talk()

类继承用 类名加（父类）即可 ，继承多个类时，时如果两个类有同样的方法，
前面的类方法会覆盖后面的方法


