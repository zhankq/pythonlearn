books = ["疯狂kotlin讲义","swift讲义","python讲义","dd"]
prices = [79,69,89]
#使用zip压缩 两个列表，从而实现并行遍历
for book,price in zip(books,prices):
	print("%s 的价格是：%5.2f" % (book,price))
#reversed()反射遍历
print(reversed(books))
print([ x for x in reversed(books)])
sorted(prices)
print(sorted(prices,reverse=True))