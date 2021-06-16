cars = {"Audi":7.9,"bens":8.4,"bmw":8.5}
#popitem()方法随机弹出一个元素，其实在底层存储来看，也是弹出最一个元素
#只是字典key-val对顺序是不可知的
print(cars)
print(cars.popitem())#每次值是固定的不会因为你每次刷新值就会变，返回一个元组
print(cars)
#将弹出值赋值给k-v
k,v = cars.popitem()
print(k,v)