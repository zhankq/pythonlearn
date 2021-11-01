a_list = [2,4,-3.4,'crazyit',23]

#对第3个元素赋值
a_list[2] = "fkit"
print(a_list)

a_list[-2] = "9527"
print(a_list)

b_list = list(range(1,5))
print(b_list)

b_list[1:3] = ['a','b']
print(b_list)
#区间大于赋值数时，【1,'a','b'】
#b_list[1:4] = ['a','b']
#print(b_list)

b_list[2:2] = ['x','y']
print(b_list)

#将其中的一段赋值为空
b_list[2:5] = [];#1,a,,,4
print(b_list)

c_list = list(range(1,10))
print(c_list)

print(c_list[2:9:2])
c_list[2:9:2] = ['a','b','c','d'] #3,5,7,9
print(c_list)

print(dir(list))
