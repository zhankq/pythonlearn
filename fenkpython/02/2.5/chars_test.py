s = 'crazyit.org is very good'
#获取索引中的2的字符
print(s[2])
#获取s中从右边开始的，索引4的字符
print(s[-4])
#获取s中从索引3到索引5（不包含）的子串
print(s[3:5])#zy
print(s[3:-5])#zyit.org is very
#获取s中从倒数第6个字符到倒数第三个字符的子串
print(s[-6:-3])#y g
#第5个开始到结束的子串
print(s[5:])#it.org is very good
#从倒第6个开始
print(s[-6:]) #y good
#从开始到索引 5 的字串
print(s[:5])#crazy
#从开始到索引 -6 的字串
print(s[:-6])#crazyit.org is ver
#用in 判断 是否包含子串
print("very" in s)
print("very23" in s)
#输出字串长度
print(len(s))
#输出最大的字符
print(max(s))
#输出最小的字符
print(min(s)) #空格
