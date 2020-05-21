'''
高阶函数使用，接收函数做为参数
'''
l = range(1,10)

def a_biger():
	newlist = []
	for i in l:
		if i>5:
			newlist.append(i)
	return newlist


def a_oushou():
	newlist = []
	for i in l:
		if i %2 == 0:
			newlist.append(i)
	return newlist

def fns(fn):
	newlist = fn()
	for i in newlist:
		print(i)

		
fns(a_biger)

fns(a_oushou)