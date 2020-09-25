fo = open("r.txt","wb")
print("文件名为：",fo.name)

#刷新缓冲区
fo.flush()

fo.close()
