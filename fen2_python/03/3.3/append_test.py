#增加列表元素
a_list = ["crazyit",20,-2]
#追加元素
a_list.append("fkit")
print(a_list) #['crazyit', 20, -2, 'fkit']
a_tuple = (3.4,5.6)
#追加元组，元组被当成一个元素
a_list.append(a_tuple)
print(a_list)
#增加一个列表，列表被当成一个元素
a_list.append(["a","b"])
print(a_list)
#如果不希望列表追加当成一个整体，而是追加列表中的元素，可以使用extend()方法
b_list = ['a',30]
#追加元组中的所有元素
b_list.extend((-2,3.1))
print(b_list)
#追加列表中的所有元素
b_list.extend(["C","R","A"])
print(b_list)
#追加区间中的所有元素
b_list.extend(range(97,100))
print(b_list)

#希望在列表中间增加元素 可使用insert()方法
c_list = list(range(1,6))
print(c_list)
#在索引3处增加字串
c_list.insert(3,"Crazy")
print(c_list)
#索引3处增加元组
c_list.insert(3,tuple('crazyit'))
print(c_list)

