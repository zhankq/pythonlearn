'''
a = int(input("a:"))
b = int(input("b:"))

print(a+b)
print(a-b)
print(a*b)
'''

'''
#查找子串出现的次数

base_str = input("字符串：")
find_str= input("子串：")

count = 0
while True:
	indexs = base_str.find(find_str)
	if indexs!=-1:
		count+=1
		countindex = indexs+1
		base_str=base_str[countindex:]
		print(base_str)
	else:
		break

print(count)
'''

s = input("first input:")

n = input("change input:")

num = int(n[0])
numstr = n[2]

ss = s[0:num]+n[2]+s[num+1:]

print(ss)