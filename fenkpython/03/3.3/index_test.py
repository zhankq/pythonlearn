
a_list = [2,30,'a','b','crazyit',30]
#定位元素30出现 的位置
print(a_list.index(30)) #1 从0开始计数

print(a_list.index(30,2)) #从索引2开始查询

print(a_list.index(30,2,4)) #从索引2到4之间定位元素30的位置 找不到 报 ValueError 


'''
a_list = [2,30,'a','b','crazyit',30]

#定义元素30出现的位置
print(a_list.index(30))

print(a_list[1])
#从索引2开始定位元素30出现 的位置
print(a_list.index(30,2))
print(a_list[5])
#d在索引2到索引4之间定位元素30出现的位置
#print(a_list.index(30,2,4))  找不到报ValueError
'''