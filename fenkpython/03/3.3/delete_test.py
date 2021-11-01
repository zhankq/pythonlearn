a_list = ["crazyit",20,-2.4,(3,4),"fkit"]
del a_list[2]  #del(a_list[2])
print(a_list)
#删除第2个到第4个元素（不包含）元素 ["crazyit",20,-2.4,(3,4),"fkit"]
del a_list[1:3]
print(a_list) #["crazyit","fkit"]

b_list = list(range(1,10))

print(b_list)
#删除<--->第3个到倒数第2个【不包含】元素，间隔为  2
#1,2,3,4,5,6,7,8,9  --->3,4,5,6,7--> 3,5,7
del b_list[2:-2:2]   #1,2,4,6,8,9
print(b_list)

del b_list[2:4] #4,6
print(b_list) #1，2，8，9

name = "abc"
#del可以删除普通 变量
print(name)
del name
#print(name) #NameError:
#remove()删除列表元素
c_list = [20,"crazy",30,-4,"crazy",3.4,30]
#删除第一次找到的30
c_list.remove(30)
print(c_list)
#删除第一次找到的 crazy
c_list.remove('crazy')
print(c_list)

#clear() ,清空列表所有的元素
c_list.clear()
print(c_list)





