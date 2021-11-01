cars = {"bmw":8.5,"bens":"44a","audi":442}
#返回所有的k-v dict_items 对象
ims = cars.items()
print(ims)
#将dict_items转换成列表
print(list(ims))
print(tuple(ims))
#访问第二个key-v 对
print(list(ims)[1])
#获取字典中所有的key，返回一个dict_keys对象
kys = cars.keys()
print(kys)
#访问第二个key
print(list(kys)[1])
#获取字典中所有的values,返回一个dict_values
vals = cars.values()
print(vals)
#访问第二个value
print(list(vals)[1])

print(type(vals))
