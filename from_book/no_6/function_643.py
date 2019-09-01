##位置参数与关键字参数
def hello_4(name,greeting="Hello",punctuation="!"):
	print("{}，{}{}".format(greeting,name,punctuation))

hello_4('hello',punctuation="===")