#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

l = []
strs = input("输入三个整数，用,分隔:")

strlpt = strs.split(',')

for i in strlpt:
    l.append(int(i))

print(sorted(l))
