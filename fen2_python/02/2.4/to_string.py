#使用str()或 repr()函数将数值转换成字符串
s1 = "这本书的价格是："
p=99.8
#字符串直接拼接数值，程序报错
#print(s1+p)
#使用str()
print(s1+str(p))
#使用repr()
print(s1+repr(p))
#repr是一个函数，它可以python的表达式的形式来表示值
st = "I will play my file"
print(st)
print(repr(st))
