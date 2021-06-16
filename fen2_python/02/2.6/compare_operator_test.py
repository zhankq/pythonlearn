print("5 是否大于 4：",5>4) #true
print("3 的 4次方 是否大于或等于90.0：",3**4 >= 90) #false
print("20 是否大于或等于20.0: ",20>=20.0)

print("5 和 5.0 是否相等",5==5.0)

print("True 和 False 是否相等：",True == False)
#True 可以当成整数1来使用 ，False被当成整数0使用
print("1 和 True 是否相等：",1==True) #True
print("0 和 False 是否相等：",0==False) #True

print(True + False)

print(False - True )

import time
a = time.gmtime()
b = time.gmtime()

print(a==b) #true
print(a is b) # false

print(id(a))
print(id(b)) #返回变量内存地址