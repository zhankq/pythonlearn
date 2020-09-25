#isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。


fo = open('r.txt',"wb")
print("文件名为：",fo.name)
ret = fo.isatty()
print("返回值：",ret)

fo.close()
