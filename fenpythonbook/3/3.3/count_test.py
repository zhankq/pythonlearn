#count 方法
a_list = [2,30,'a',[5,30],30]
print(a_list.count(30))
#index 判断某个元素在列表中出现的次数
a_list=[2,30,'a','b','crazyit',30]
indexs = a_list.index(30)
print(indexs)
#从索引2开始，定位元素30出现的位置
indexs = a_list.index(30,2)
print(indexs)
