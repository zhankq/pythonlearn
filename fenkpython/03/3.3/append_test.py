a_list = ["crazyit",20,-2]

#追加元素
a_list.append("fkit")
print(a_list)

a_tuple=(3.4,5.6)
a_list.append(a_tuple)
print(a_list)

a_list.append(["a","b"])
print(a_list)

a_list.append(range(1,3))
print(a_list)


#不将追加的元素当成一个整体时，使用 extend方法
b_list = ["a",30]
b_list.extend((-2,3.1))
print(b_list)
b_list.extend(["C","R","A"])
print(b_list)
#追加区间中的所有元素
b_list.extend(range(97,100)) #
print(b_list)
#insert()方法,在指定位置插入元素
c_list = list(range(1,6))
print(c_list) #[1,2,3,4,5]
#在索引3处插入字符串
c_list.insert(3,"CRAZY")#1,2,3,"CRAZY",4,5
print(c_list)
#在索引3处插入元组
c_list.insert(3,(6,7))#1,2,3,(6,7),"CRAZY",4,5
print(c_list)

c_list.insert(3,[8,9])#1,2,3,[8,9],(6,7),"CRAZY",4,5
print(c_list)

c_list.insert(3,range(10,11))#1,2,3,range(10,11),[8,9],(6,7),"CRAZY",4,5
print(c_list)







