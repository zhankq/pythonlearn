第五章，条件、循环及其他语句

s={"name":'wjc123',"age":"45"}
key,val=s.popitem()

返回　key=name,val=wjc123
a,b,*rest=[1,2,3,4]

>>> a,b,*rest=[1,2,3,4]     
>>> rest
[3, 4]
带＊号的值总是在列表里

name = input("what's your name:")
status="friend" if name.endswith("Gumby") else "stranger"

类似三元运算符，　if 条件为真返回提供的第一个值，（这里为friend）
否则为第二个值，此处为stranger

is　还表示引用,即是是否为同一个对象而不止是　内容相等
例：　x=y=[1,2,3]
z=[1,2,3]
x==z  [True]
x is z [False]

x is y [True]

assert 断言语句，当条件满足时程序结束

类似　
if not condition:
    crash program
    
例：
>>> age=100
>>> assert age<100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

zip 将两个序列缝合起来
例>>> names =["anne","beth","george","damon"]
>>> ages= [12,45,32,10]
>>> zip(names,ages)
<zip object at 0x0000022B2CB83DC8>
for name,age in zip(names,ages):
    print(name,age)

pass 什么了不做 其实也可用字符串代替。

exec 函数 将字符串做代码执行

eval 功能类似，但会产生返回值

