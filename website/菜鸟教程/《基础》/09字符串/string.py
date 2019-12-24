para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
'''
print(para_str)
s=' rr '
s.strip() #去除两边的空格
'''
import  datetime
import time
day = datetime.datetime.today().date()
ts = int(time.mktime(time.strptime(str(day), '%Y-%m-%d')))


print(ts)


