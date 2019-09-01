count = 0
def fnt(n):
	global count
	count+=1
	if n==1:
		return 1
	else:
		return n * fnt(n-1)


print(fnt(51))

print(count)