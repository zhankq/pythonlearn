def is_subsequence(a,b):
	b=iter(b)
	print(b)

	gen = (i for i in a)
	print(gen)

	for i in gen:
		print(i)

	gen = ((i in b) for i in a )
	print(gen)

	for i in gen:
		print(i)

	print(((i in b) for i in a))


	return all(((i in b) for i in a))

#print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5])) #返回false 因为 12 行调用 了一次了
