#coding=utf-8
'''
while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：
-------------------demo--------------
count=0
while count<5:
    print(count,"smaller 5")
    count = count+1
else:
    print(count,"biger 5")
-------------------demo--------------

简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中，
---------------------------
i = 10
while (i): i=i-1
print(i)
-------------------------------

for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
------------------------------------------
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    if x=='C++':
        continue

    print(x)
else:
    print('no out put')
------------------------------------

循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
'''
