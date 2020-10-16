s = input("输入多个字串,分隔：")

tuples = s.split(',')

print("去除重复：",list(dict.fromkeys(tuples)))

f=(1,2,4)
print(f.__hash__())


print(tuples)


