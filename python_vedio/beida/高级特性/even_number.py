#关于生成器函数使用
def even_number(max):
    n=0
    while n< max:
        yield n
        n += 2

for i in even_number(10):
    print(i)
    break
