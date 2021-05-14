#以0x或0X开头的整型数值是十六进制形式的整数
hex_value1 = 0x13
hex_value2 = 0XaF
print("hexValue1 的值为：",hex_value1)
print("hexValue2 的值为：",hex_value2)
#以0b或0B开头的整形数值是二进制形式的整数
bin_val = 0b111
print('bin_val 的值为：',bin_val)
bin_val = 0B101
print("bin_val 的值为：",bin_val)
#以 0o或0O开头的整型数值是八进制的整数
oct_val = 0o54
print("oct_val 的值为：",oct_val)
oct_val = 0O17
print("oct_val 的值为：",oct_val)
#数值增加下划线作为分隔符，不会影响数值本身
one_million = 1_000_000
print(one_million)
price = 234_234_234 #234234234
android = 1234_1234 #12341234
print(price)
print(android)
