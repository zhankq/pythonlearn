#定义一个字符串
hello = "hello"
print("hello是否是str类的实例",isinstance(hello,str))
#是否为object类子类的实例，输出True
print('"Hello" 是否是object类的实例：',isinstance(hello,object))
#str是object类的子类输出True
print('str是否是object类的子类:',issubclass(str,object))
#"hello"不是tuple类及其子类的实例 ，输出false
print('"hello"是否是tuple类的实例：',isinstance(hello,tuple))
#str不是tuple类的子类，输出false
print('str是否是tuple类的子类：',issubclass(str,tuple))
#定义一个列表
my_list = [2,4]
#[2,4]是list类的实例，输出True
print('[2,4]是否是list类的实例：',isinstance(my_list,list))
#[2,4]是object类的子类的实例，输出True
print('[2,4]是否是object类及其子类的实例：',isinstance(my_list,object))
#list是object类的子类，输出True
print("list是否是object类的子类：",issubclass(list,object))
# 【2, 4】不是tuple类及其子类的实例输出 False
print('[2, 4]是否是tuple类及其子类的实例：',isinstance([2, 4],tuple))
# list不是tuple类的子类
print('list是否是tuple类的子类：',issubclass(list,tuple))
data = (20, 'fkit')
print('data是否为列表或元组:',isinstance(data,(list,tuple)))
# str不是list或者tuple的子类，输出False
print('str是否为list或tuple的子类：',issubclass(str,(list,tuple)))
# str是list或tuple或object的子类，输出True
print('str是否为list或tuple或object的子类 ',issubclass(str,(list,tuple,object)))