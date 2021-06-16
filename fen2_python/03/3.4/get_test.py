cars = {"bms":44,"bens":443,"audi":4.6}
#通过字典的get()方法来获取
print(cars.get("bms"))
#不存在的报none
print(cars.get("bmsd"))
print(cars["bens"])
#不存在报错
#print(cars["bensd"])
