try:
	#print(1/0)
	# print(a)
	4+"d"
except ZeroDivisionError:
	print("除 0 异常")
except NameError:
	print("NameError")
except Exception as e: #except Exception: 作用相同
	print("啥都不是",e)
else:
	print("正常的")
finally:
	print("总要执行")