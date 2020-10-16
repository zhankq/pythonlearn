#get()方法key不存在时，会返回None,方括号语法的加强版
dict6=dict(spinach=1.39,cabbage=2.59)

s1=dict6.get("a")
print(s1)
s2 = dict6.get("spinach")
print(s2)
s3 = dict6["spinach"]
print(s3)
#update方法使用
dict6.update({"b":'BBBBB',"spinach":"----"})
print(dict6)

