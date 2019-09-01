##字符串使用
f的使用

from math import e
print(f"contansts {e}.")

>>>contansts 2.718281828459045.
替换字段名，顺序字段与参数配对可以合起来使用

"{foo} {} {bar} {}".format(1,2,bar=4,foo=3)

还可以在列表中使用
fullname = ["Alfred","smoketoomuch"]
s = "Mr {name[0]}".format(name=fullname)
Mr Alfred

"{num:10}".format(num=3)

指定对齐方式左对齐，右对齐，和居中，可分别用<,> 和^
"{:>10}".format(122)

center
"sd".center(2)

find()
找到返回索引位置，否则返回-1

join 合并内容都必须是字符串
sq = [1,3]
sp='+'
sp.join(sq)
报错

sq = [‘1’,’3‘]
sp='+'
sp.join(sq)

#判断字符串是否小写
"FSs".islower()

title()首字母大写
"talk is cheap".title() #'Talk Is Cheap'

replace 替换字串

split 拆分字符串
'１+２+3'.split('+') #['１', '２', '3']

strip() 去除两边空格
lstrip()  去除左边空格
rstrip()  去除右边空格
