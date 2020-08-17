#直接对 False 求非运算
print(not False)
#and
print(2>1 and 4>3)
#or
print(2<1 or 4>3)

bookName="疯狂Python"
price =79
version="正式版"

if bookName.endswith("Python") and (version=="正式版" or price<50):
	print("打算购买这栖书")
else:
	print("No!")