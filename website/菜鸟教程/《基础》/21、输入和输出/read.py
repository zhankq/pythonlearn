#!/usr/bin/python3
# 打开一个文件
f=open("foo.txt","r")

# str = f.read()  读取整个文件
# str = f.readline() #读取单行
f.readlines() #读取所有的行
print(str)

f.close()
