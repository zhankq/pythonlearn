'''
def print_params_4(x,y,z=3,*pospar,**keypar):
	print(x,y,z)
	print(pospar)
	print(keypar)


print_params_4(1,2,33,'a','b','c',keya="keya",keyb="kebe");
'''

#通过＊来调用

def power(x,y,*other,**others):
	if other:
		print("one * other",other)
	if(others):
		print("two * others",others)

	return pow(x,y)

s = [1,2]
f = power(3,2,*s) #one * other (1, 2)   元组形式
print(f)
ｄ= {'a':'bb','c':'dd'}

f = power(3,2,*s,**d) #two * others {'a': 'bb', 'c': 'dd'}
print(f)

