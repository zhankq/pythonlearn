#!"C:\Users\zhank\AppData\Local\Programs\Python\Python37\python.exe"
import cgi,os
import cgitb
cgitb.enable()


form = cgi.FieldStorage()

#获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
   # 设置文件路径  ，这个是windows下的用法
   fn = os.path.basename(fileitem.filename)
   #linux/unix 下的使用方式
#   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('tmp/' + fn, 'wb').write(fileitem.file.read())

   message = '文件 "' + fn + '" 上传成功'
   
else:
   message = '文件没有上传'
   
print ("""\
Content-Type: text/html\n
<html>
<head>
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))