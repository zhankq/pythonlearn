
a_range = range(10)
c_generator = (x*x for x in a_range if x % 2 ==0)
for i in c_generator:
	print(i,end="\t")
print()

src_a = [30,12,66,34,39,78,36,57,121]
src_b = [3,5,7,11]
result = [(x,y) for x in src_b for y in src_a if y % x ==0]
print(result)
