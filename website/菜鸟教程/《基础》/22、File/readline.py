fo= open('r.txt','r+')

print("文件名：",fo.name)

line = fo.readline()
print("读取第一行 %s" % (line))

line = fo.readline(5)

print("读取的字符串为：%s" % (line))

fo.close()