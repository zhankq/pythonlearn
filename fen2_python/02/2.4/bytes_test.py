#创建一个空的bytes
b1 = bytes()
#创建一个空的bytes值
b2 = b''
#通过b前缀指定hello 是bytes 类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
#调用bytes 方法将字符串转换成bytes对象
b4 = bytes("我爱Python编程",encoding='utf-8')
print(b4)
b5 = "学习Python很有趣".encode("utf-8")
print(b5)
st = b5.decode('utf-8')
print(st)
b="#通过b前缀指定hello \n是bytes 类型的值"
print(b)
s2 = "商品名\t\t单价"
s3="疯狂java讲义\t108"
print(s2)
print(s3)
