##字典的使用，
键值必须是任何不可变的类型所以列表类型是不允许的
'''
phone_book = {'beth':'9102','Alice':2341}
print('beth"s phone is {Alice}.'.format_map(phone_book))
'''
format 可以映身字典

浅复制，　.copy()

副本中的列表改变时，依然会影响主体信息

.deepcopy　深复制


fromkeys 创建一个字可以指定键值
dict.fromkeys(["name","good"],["tt"])
#{'name': ['tt'], 'good': ['tt']}
dict.fromkeys(["name","age"])
#{'name': None, 'age': None}
.get()
访问字典中的键比直接访问更友好些，直接访问如果键不存在会报错，而get不会他会返回Ｎone


pop 获取指定的键值　并将该值从列表中删除
popitem 随机弹出一个字典项
