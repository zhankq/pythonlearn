cars = {"bms":65}
#设置默认值，key 不存在新增返回，存在直接返回并不修改默认值
print(cars.setdefault("porsche",9.2))
#存在直接返回并不修改默认值,返回依然是65
print(cars.setdefault("bms",9.2))