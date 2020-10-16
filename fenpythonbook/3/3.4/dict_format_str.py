#在字符串模板中使用key
temp = "书名是:%(name)s,价格是:%(price)0.2f,出版社是:%(publish)s"
book = {"name":"疯狂python讲义","price":88.9,"publish":"电子社"}
book2 = {"name":"疯狂Java讲义","price":8.9,"publish":"子社"}
print(temp % book)

print(temp % book2)
