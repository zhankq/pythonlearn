def test():
	for i in range(10):
		for j in range(10):
			print("i的值 是:%d,j的值 是:%d" % (i,j))
			if j==1:
				return 
			print("return后的输出语句")

test()


print("ddd"+"ss")