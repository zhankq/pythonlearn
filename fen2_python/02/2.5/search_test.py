s = 'crazyit.org is good siteb'
#判断 s 是否以crazyit 开头
print(s.startswith('crazyit'))
#判断 s是否以site结尾
print(s.endswith('site'))
#查找s中org出现的位置
print(s.find('org'))
#从索引9处开始查找 org 出现的位置
print(s.find('org',9)) #-1
#从索引9处开始查找 org 出现的位置
#print(s.index('org',9)) #未找到引发错误
#将字符串中的所有it替换成xxxx
print(s.replace('it','xxxx'))
#将字符串中的一个it替换成xxxx
print(s.replace('it','xxxx',1))
#定义翻译映射表
table = {97:945,98:946,116:964}
print(s.translate(table))
#table2 = str.maketrans('abt','αβτ')
#print(table)
table2 = str.maketrans('abt','123')

print(s.translate(table2))
