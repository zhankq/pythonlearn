#同时能元组进行加法，乘法
order_endings = ("st","nd","rd")\
+("th",)*17+("st","nd","rd")\
+("th",) *17+("st",)

print(order_endings)

day = input("输入日期:(1-31):")
day_int = int(day)
print(day+order_endings[day_int-1])

#无组
print(("d",))
#字符串
print(("d"))