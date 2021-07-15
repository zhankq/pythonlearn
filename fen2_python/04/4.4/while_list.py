src_list = [12,45,34,13,100,24,56,74,109]
a_list = [] #整除3的元素
b_list = [] #余1的元素
c_list = [] #余2的元素
#只要 src_list 还有元素，就继续 执行循环体
while  len(src_list):
	ele = src_list.pop()
	#如果ele
	if ele % 3 ==0:
		a_list.append(ele)
	elif ele % 3 ==1:
		b_list.append(ele)
	else:
		c_list.append(ele)

print("整除3：",a_list)
print("整除3余1：",b_list)
print("整除3余2：",c_list)

