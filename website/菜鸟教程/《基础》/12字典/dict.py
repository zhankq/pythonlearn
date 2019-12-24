#!/usr/bin/python3
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

''''
del dict['Name'] # 删除键 'Name'
dict['School'] = "学校"

dict.clear()     # 清空字典
del dict         # 删除字典

dict['1']='123'
dict[3]='123'

print(dict)
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

f=[1,2]
f[1] = 'd'
print(f[1])
'''
'''
radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表

lst = dict.keys()
print(list(lst))
#print(tuple(lst))
'''
#radiansdict.values()
#返回一个迭代器，可以使用 list() 来转换为列表

vlst = dict.values()
print(list(vlst))
