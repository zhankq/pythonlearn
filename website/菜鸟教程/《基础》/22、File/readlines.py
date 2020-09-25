fo= open('r.txt','r+')

print("文件名：",fo.name)

for line in fo.readlines():
    line = line.strip()
    print("读取的数据为：%s" % (line))

#关闭文件
fo.close()