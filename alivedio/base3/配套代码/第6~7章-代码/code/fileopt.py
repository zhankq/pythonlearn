file_name = r"D:\python_learn\alivedio\base3\配套代码\第6~7章-代码\code\demo.txt"
# try:
with open(file_name, 'rb') as fileobj:
# with open('demo.txt','rb') as fileobj:
	fileobj.seek(55,1)
	# fileobj.seek(80,0)
	print(fileobj.tell())

	print(fileobj.read())
# except:
# 	print(f'{file_name} 文件不存在~~')

import os
print(os.listdir())
try:
	os.remove('a/ad.txt')
	os.rmdir('a')
except:
	print("=====")
