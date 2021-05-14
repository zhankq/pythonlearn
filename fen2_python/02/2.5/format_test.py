user = "Charlis"
age = 8
#格式化字符串中有两个占位符，第三部分也应该提供两个变量
print("%s is a %s years old boy" % (user,age))
num = -28
print("num is：%6i" % num)

print("num is：%6d" % num)

print("num is：%6o" % num)

print("num is：%6x" % num)

print("num is：%6x" % num)

print("num is：%6X" % num)

print("num is：%6s" % num)

num2 = 30
print("num2 is :%06d" % num2 )

print("num2 is %+6d" % num2)

print("num2 is %-6d" % num2)
my_value = 3.001415926535
#最小宽度为8，小数点后保留3位
print("my_value: %8.3f" % my_value)
#最小宽度 为8，小数点后保留3位，左边补0
print("my_value is :%08.3f" % my_value)
the_name = "Charlie"
#只保留3个字符
print("the name is:%.3s" % the_name)
#只保留2个字符,最小宽度为10
print("the name is: %10.2s" % the_name)
