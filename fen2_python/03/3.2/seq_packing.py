#序列包，将10,20,30封装成元组后赋值给vals
vals = 10,20,30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1,10,2))
#序列解包：将 a_tuple 元组的各元素依次赋值给 a,b,c,d,e变量
a,b,c,d,e = a_tuple
print(a,b,c,d,e) #1 3 5 7 9

a_list = ["fkit","crazyit"]
a_str,b_str = a_list
print(a_str,b_str)

#first ,second保存前两个元素，rest列表包含剩下的元素
first,second,*rest =  range(10)
print(first,second,rest)
#last保存最后一个元素，begin保存前面剩下的元素
*begin,last = range(10)
print(begin,last) #[0, 1, 2, 3, 4, 5, 6, 7, 8] 9
#first 保存第一个元素，last保存最后一个元素，middle 保存中间剩下的元素
first,*middel,last = range(10)
print(first)
print(middel)
print(last)