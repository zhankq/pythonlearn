a_list = [2,3,-3.4,'crazyit',23]
#对第3个元素赋值
a_list[2] = "fkit"
print(a_list)
#对倒数第2个元素赋值
a_list[-2] = 9527
print(a_list)

b_list = list(range(1,5))
print(b_list)
#t第二个到第四个元素赋值
b_list[1:3] = ['a',"b"]
print(b_list)
#将第3个到第3个元素赋值相当于插入元素
b_list[2:2] = ["x","y"]
print(b_list)
#u将第3个到第6个元素赋值为空列表就是删除元素
b_list[2:5] = []
print(b_list)
#使用slice语法赋值时，不能使用单个值 ，如果使用字符串，python会自动将其当成序列来处理。
b_list[1:4] = "Charlie"
print(b_list)

c_list = list(range(1,10))
#指定step为2,被赋值的元素有4个，因此用于赋值列表也必须有4个元素
c_list[2:9:2] = ["a","b","c","d"]

print(c_list)