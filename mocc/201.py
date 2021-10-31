def sum1(num):
	sums = 0
	for i in range(1,num+1):
		sums+=i
	return sums

def sum2(num):
	if num % 2 ==0:
		sums=0
	else:
		sums=num//2+1
		
	for i in range(0,num//2):
		sums += (1+num)
	return sums

import time

nums = 100000001
start = time.time()
f1 = sum1(nums)
print(f1)
used = time.time() - start

print("sum1 启动时间：",used)


print()

start = time.time()
f1 = sum2(nums)
used = time.time() - start
print(f1)
print("sum2 启动时间：",used)
