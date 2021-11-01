#print(value,...,sep=" ",end="\n",file=sys.stdout,flush=False)
user_name = "Charlie"
user_age = 8
#同时输出多个变量和字符串
print("读者名：",user_name,"年龄:",user_age)
#输出多个变量和字符串，指定分隔符
print("读者名：",user_name,"年龄:",user_age,sep='|')
#print函数的end参数默认值为"\n"
#设置end参数，指定输出之后 不再换行
print(40,"\t",end="")
print(50,"\t",end="")
print(60,"\t",end="")
#file 参数默认值为sys.stdout该默认值 代表了系统 标准输出，也就是屏幕
#设置file参数 将内容输出到某个文件
f = open("poem.txt","w") #打开文件以便写入
print("沧海月明珠有泪",file=f)
print("蓝田日暖玉生烟",file=f)
f.close()
#flush 参数用于控制输出缓存，该参数 一般保持为false即可，这样可以获得较好的性能