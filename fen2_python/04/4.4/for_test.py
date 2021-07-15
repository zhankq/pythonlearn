s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1
#使用for in 循环
for num in range(1,mx+1):
	result *= num
print(result)