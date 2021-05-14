s = " this is a puppy "
#删除左边的空白
print(s.lstrip())
#删除右边的空白
print(s.rstrip())
#删除两边的空白
print(s.strip())
#删除字符串前后指定的字符的功能
s2 = 'idtw think it is a scarecrow'
#删除左边的i,t,o,w
print(s2.lstrip('itow')) #dtw think it is a scarecrow

s2 = 'itw think it is a scarecrow'
print(s2.lstrip('itow'))# think it is a scarecrow
#删除右边的i,t,o,w
print(s2.rstrip('itow'))#itw think it is a scarecr
#删除右边的i,t,o,w
print(s2.strip('itow')) #think it is a scarecr
