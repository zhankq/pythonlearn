my_dict = {"语文":89,"数学":92,"英语":80}
#通过items()方法遍历所有的k-v对
for key,value in my_dict.items():
	print("key:",key)
	print("value:",value)
print('------------------------')
#通过keys()方法遍历所有的key
for key in my_dict.keys():
	print("key:",key)
	#通过key获取value
	print("value:",my_dict[key])
print('-------------------------')
#通过values()方法遍历所有的values
for value in my_dict.values():
	print("value:",value)