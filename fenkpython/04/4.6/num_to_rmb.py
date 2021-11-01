#数字 转 人民币的讲法
'''
把一个浮点数分解成整数部分与小数部分的字符串
num 是需要被分解的浮点数
返回分解出来的整数部分与小数部分
第一个数组元素是整数部分，第二个数组元素是小数部分
'''
def divide(num):
	#强制转换类型为int ，即得到它的整数部分
	integer = int(num)
	#浮点数减去整数部分，小数部分乘以100后再取得保留了2位的小数
	fraction = round((num-integer) * 100)
	#返回两个数数字符串
	return (str(integer),str(fraction))

han_list = ["零" , "壹" , "贰" , "叁" , "肆" ,  "伍" , "陆" , "柒" , "捌" , "玖"]
unit_list = ["十" , "百" , "千"]

'''
把一个四位数的数字字符串变成汉字字符串
num_str 需要被转换成四位数字的字符串
返回四位的 数字 字符串被转换成汉字字符串
1234
'''
def four_to_hanstr(num_str):
	result = ""
	num_len = len(num_str)
	#依次遍历数字 字符串的每一位数字
	for i in range(num_len):
		#把字符串转成数值
		num = int(num_str[i])
		#如果不是最后一个数字，且数字不为零，则需要添加单位（千、百、十）
		if i != num_len-1 and num != 0:
			result += han_list[num] + unit_list[num_len-2-i]
		else:#如果是个位数不要添加单位
			result+=han_list[num]

'''
把数字
'''