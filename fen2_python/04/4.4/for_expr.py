#[表达式 for 循环计数器 in 可迭代对象]
a_range= range(10)
a_list = [x*x for x in a_range]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(a_list)
b_list = [x*x for x in a_range if x % 2 ==0]
print(b_list)
c_generator = (x * x for x in a_range if x % 2 ==0)
#使用for 循环迭代生成器
for i in c_generator:
	print(i,end="\t")
print()
#用for 循环表达式 使用多个循环
d_list = [(x,y) for x in range(5) for y in range(4)]
#d_list列表包含20个元素 功能类似如下 的代码，类似的代码也支持三层循环
'''
dd_list = []
for x in range(5):
	for y in range(4):
		dd_list.append((x,y))
'''
print(d_list)

#多 个循环加上if 条件
src_a = [30,12,66,34,39,78,36,57,121]
src_b = [3,5,7,11]

result = [(x,y) for x in src_b for y in src_a if y%x == 0]
print(result)





