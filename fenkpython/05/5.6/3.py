def is_leap(year):
    if year % 4 ==0 or year % 400 ==0:
        return True
    return False

years = 2020
print("%d 年是闰年吗？" % years,"是" if is_leap(years) else "不是" )