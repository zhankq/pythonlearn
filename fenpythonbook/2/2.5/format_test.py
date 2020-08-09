user = "Charli"
age = 8
#格式化字符串吕有两个占位符，第三部分也应该提供两个变量
print("%s is a %s years old boy"%(user,age))


'''
num=28

#当中的 6 表示 输出宽度，也可理解 除输出外用0填充
#i/d,转换为带符号的十进制整数
print("num is: %6i" % num)
print("num is: %06d" % num)
#o 八进制整数
print("num is: %6o" %num)
#x/X 转换为带符号的十六进制形式的整数
print("num is: %6x" %num)
print("num is: %6X" %num)
#使用str 转为字符串
print("num is: %6s" %num)

################################

num2 = 30
#最小宽度为6左边补0
print("num2 is: %06d" %num2)
#最小宽度为6，左边补0总带上符号
print("num2 is:%+6d" % num2)
#0 表示不补充空格，而是补充0
print("num2 is:%-6d" % num2)
'''
my_value = 3.001415926535
#最小宽度为8，小数点后保留3位
print("my_value is: %8.3f" % my_value)
#最小宽度为8，小数点后保留3位，左边补0
print("my_value is: %08.3f" % my_value)
#最小宽度为8，小数点后保留3位，左边补0，始终 带符号
print("my_value is %+08.3f" % my_value)
the_name = "Charlie"
#只保留3个字符 
print("the name is: %.3s" % the_name)
#保留2个字符，最小宽度为10
print("the name is: %10.2s" % the_name)

