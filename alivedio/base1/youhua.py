from time import *
begin = time()
i = 2
while i <= 100000 :
	flag = True
	j = 2
	while j <= i ** 0.5: #开方
		if i % j == 0:
			flag = False
			break
		j += 1
	if flag:
		pass
	i += 1

end = time()

print("程序执行的时间: ",end-begin , "秒")
