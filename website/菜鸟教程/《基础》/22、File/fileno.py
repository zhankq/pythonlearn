fo = open("r.txt","wb")
print("文件名为：",fo.name)

fid = fo.fileno()
print("文件描述符为：",fid)

fo.close()
