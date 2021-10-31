year = int(input("year:\n")) #输入年
month = int(input("month:\n"))#输入月
day = int(input("day:\n"))#输入日

'''
程序分析：以3月5日为例，应该先把前两个月的加起来，
然后再加上5天即本年的第几天，特殊情况，
闰年且输入月份大于2时需考虑多加一天： 闰年 2月为29天
'''
#每一个月到11月
months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <= 12 :
    sum = months[month - 1]
else:
    print('data error')

sum += day

leap = 0
#判断 是否为闰年
if (year % 4==0) or ((year % 4==0) and (year % 100 != 0)):
    leap = 1
#如果是闰年且是２月以上的就额外加１
if (leap==1) and (month > 2) :
    sum += 1

print("it is the %dth day." % sum)