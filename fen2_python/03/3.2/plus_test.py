#加法
a_tuple = ("crazyit",20,-1.2)
b_tuple = (127,"crazyit","fkit",3.33)
#计算元组相加
sum_tuple = a_tuple + b_tuple;
print(sum_tuple) # ('crazyit', 20, -1.2, 127, 'crazyit', 'fkit', 3.33, 20)
print(a_tuple) #无改变
print(b_tuple) #无改变
#两个元组相加
print(a_tuple + (-20,-30)) # ('crazyit', 20, -1.2, -20, -30)
#元组与列表不能直接相加
#print(a_tuple+[-20,-30])
#计算列表相加
a_list = [20,30,50,100]
b_list = ["a","b","c"]
sum_list = a_list+b_list
print(sum_list)
print(a_list+["dd"])


