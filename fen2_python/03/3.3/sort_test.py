a_list = [3,4,-2,-30,14,9.3,3.4]

#对列表元素排序
a_list.sort()
print(a_list)
b_list = ["Python","Swift","Ruby","Go","Kotlin","Erlang","Erlanh"]
#按字符串的编码进行排序
b_list.sort()
print(b_list)
#按字符串长度比较大小
b_list.sort(key=len)
print(b_list)
#反向排排序默认是从小到大，True时则是从大到小
a_list.sort(reverse=True)
print(a_list)

b_list.sort(key=len,reverse=True)
print(b_list)