#去除重复的字符串
s = input("输入n个字符串，用逗号分隔:")

lists = list((s.split(",")))

print(lists)
newdict = {}

for item in lists:
    newdict[item] = item

klist = list(newdict.keys())

print(klist)

#print(dict(lists))

