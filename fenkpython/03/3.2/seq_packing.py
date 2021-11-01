#序列封包，将10，20，30封装成元组后赋值给vals
vals = 10,20,30
print(vals)
print(type(vals))

print(vals[1])
a_tuple = tuple(range(1,10,2))
print(a_tuple)
#序列解包
a,b,c,d,e = a_tuple
print(a,b,c,d,e)

a_list = ["fkit","crazyit"]
#序列解包
a_str,b_str = a_list
print(a_str,b_str)
#将值  10,20,30 依次 赋值给 x,y,z
x,y,z = 10,20,30
#相似
xyz=10,20,30
x,y,z = xyz
#交换变量
x,y,z = y,x,z
print(x,y,z)
#first,second保存前两个元素，rest列表包含剩下的元素
first,second,*rest = range(10)
print(first,second,rest)
#last保存最后一个元素
*begin,last=range(10)
print(begin,last)
#first,第一个元素，last 最后一个元素，*middle中间的元素
first,*middle,last = range(10)
print(middle)






