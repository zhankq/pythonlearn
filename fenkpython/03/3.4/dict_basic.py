ls = [1,2]
f = dict(a="aaa",b="bbb")
print(f)
print("a" in f)
f["a"] = "1111"
print(f)
del(f["b"])
print(f)
#clear()清空字典
f.clear()
print(f)
