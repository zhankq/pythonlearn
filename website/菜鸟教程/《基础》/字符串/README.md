https://www.runoob.com/python3/python3-string.html

##字符串
[ : ]	截取字符串中的一部分，遵循左闭右开原则，
str[0,2] 是不包含第 3 个字符的。
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

Python三引号
python三引号允许一个字符串跨多行，字符串中可以包含换行符、
制表符以及其他特殊字符。

来自简明python[https://bop.mol.uno/07.basics.html]
如果你希望在一行物理行中指定多行逻辑行，那么你必须通过使用分号(;)来明确表明逻辑行或语句的结束。

i = 5
print(i)
实际上等同于
i = 5;
print(i);
i = 5; print(i);
然而，我强烈建议你对于每一行物理行最多只写入一行逻辑行。
这个观点就是说你不应该使用分号。实际上，我从未在 Python 程序中使用、
甚至是见过一个分号。
来自简明python[https://bop.mol.uno/07.basics.html]
