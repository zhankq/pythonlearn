s = "crazyit.org is a good site"
#判断s 是否以crazyit开头
print(s.startswith("crazyit"))
#判断s是否以site结尾
print(s.endswith("site"))
#查找s中org出现的位置
print(s.find("org"))
#查找s中org出现的位置  ---功能相同但发生找不出数据时，前者返回-1，后者引发ValueError错误
print(s.index('org'))
#查找从索引9处开始 org 出现的位置
#print(s.index('org',9))
#查找从索引9处开始 org 出现的位置
print(s.find('org',9))
#将字符串中的所有it替换成XX
print(s.replace('it',"xxx"))
#将字符串中的1个it替换成xxx
print(s.replace('it',"xxx",1))
#定义翻译映射表：97(a)->945(α),98(b)->946(β),116(t)->964(τ)
table = {97:945,98:946,116:964}
print(s.translate(table))
#生成映射表
table = str.maketrans("crazyit","abcdefg")
print(table)

print(s.translate(table))

#split字符串分割后成列表
#用空白分割
print(s.split())
#使用空白对字符串进行分割，最 多只分割前两个单词
print(s.split(None,2)) #['crazyit.org', 'is', 'a good site']
#使用.进行分割
print(s.split('.'))

mylist = s.split()
#使用‘/’作为分割符，将mylist连接成字符串
print('/'.join(mylist))
#使用‘，’作为分割符，将mylist连接成字符串
print(','.join(mylist))



