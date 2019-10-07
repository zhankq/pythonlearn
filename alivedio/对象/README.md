像 int,float 都属于类
isinstance(obj,class) 判断一个对象是否是一个类的实例obj对象，class类名
类也 一个对象
是一个type类型的对象
class Mc
    pass
print(id(Mc),type(Mc))

类创建对象的流程
1、创建一个变量mc
2、在内存中创建一个新对象
3、执行类的代码块中的代码【只在类定义时执行一次】
4、__init__(self)方法执行【对象创建即执行】
5、将对象的ID赋值给变量
1、id
2、type
3、value
如果方法调用，默认传递一个参数，所以方法至少要定义一个形参  


以__开头的特殊方法【魔术方法】
特殊不需要自己调用，不要尝试去调用特殊方法
特殊什么时候调用
特殊方法作用

封装
    隐藏属性
    __双 下划线开头隐藏，只能在内部访问
    其本质是将名字改了，改成了 _类名__属性名
    即 __name --> _Person__name
    
    装饰器
    @property
    def name(self):
        print("get execute")
        return self._name
#可以直接这么调用
    print(one.name)

 #setter 方法的装饰器：@属性名.setter
    @name.setter
    def name(self,name):
        self._name = name
               
 one.name='1283'


继承
定义时 
子类（父类）：
    pass
    
    
检查一个类是否是另一个类的子类
issubclass()    

方法重写
子类覆盖父类的同名方法

super()父类



__bases__这个属性可以用来鹳狸猿取当前类的所有父类

多类继承会使子类拥有多个父类，使子类拥有其他父类的方法
就尽量避免使用多继承，前面的类会覆盖后面的类的方法
例 
f= aobj(son1obj,son2obj) 

f.test() #当两个类都有test方法时，则调用son1obj



封装
 - 确保对象中的数据安全
继承
 - 保证对象的可扩展性
多态
 - 保证程序的灵活性

类属性可以用类或类的实例来访问到

类方法
def test_2:
#类方法
    #类方法的第一个参数 cls ，也会自动传递 ，cls就是当前的类对象
    #类方法与实例方法的区别，实例方法的第一个参数是self，类方法的第一个参数是cls
    #可以用实例方法也可以类方法的时候用。
    @classmethod
    def test_2(cls):
        print(cls.count)
        
#静态方法
    #@staticmethod 来修饰的方法属于静态方法
    @staticmethod
    def test_3():
        print("test_3 执行了~~~~")
        
#静态方法与类无关的方法，她只是一个保存在当前 类中的函数 
#静太方法一般是一些工具方法，和当前类无关
       

在python有自动的垃圾回收机制，所以不用手动处理

#魔术方法，它会在对象被垃圾回收前调用
def __del__(self):
        pass

打印对象时，调用魔术方法__str(self)__        
print(obj)

