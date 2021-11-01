a_list = [3,4,-2,-30,14,9.3,3.4]
#对列表元素排序
a_list.sort()

print(a_list)
b_list = ["Python","Swift","Ruby","Go","Kotlin","Erlang","Z"]
b_list.sort()

print(b_list)
b_list.sort(reverse=True,key=len)

print(b_list)
