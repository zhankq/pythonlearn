s = "crazyit.org is a good site"
#使用空白对字符串进行分割
print(s.split()) #输出 ['crazyit.org', 'is', 'a', 'good', 'site']
#使用空白对字符串进行分割，最多分割前两个单词
print(s.split(None,2))#输出['crazyit.org', 'is', 'a good site']
#使用点进行分割
print(s.split('.'))

mylist = s.split()
#使用'/'作为分隔符，将mylist连接成字符串
print('/'.join(mylist))
#使用,作为分割符，将mylist连接成字符串
print(','.join(mylist))
