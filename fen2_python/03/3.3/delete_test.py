a_list = ["crazyit",20,-2.4,(3,4),"fkit"]
#删除第3个元素
del a_list[2]
print(a_list) #"crazyit",20,(3,4),"fkit"
#删除从第2 个到第4个（不包含）元素
del a_list[1:3]  #"crazyit","fkit"
print(a_list)

b_list = list(range(1,10))
#删除第3个倒数第2个，间隔为2
del b_list[2:-2:2] #[1, 2, 4, 6, 8, 9]
print(b_list)

del b_list[2:4]
print(b_list)
name = "a"
del name
#print(name) 报错
#remove() 只能删除列表的元素
c_list = [20,3.4,"crazyit",30,-4,3.4]

c_list.remove(3.4) #删除第一次找到的元素
print(c_list) 
c_list.remove('crazyit') #删除"crazyit"
print(c_list) 