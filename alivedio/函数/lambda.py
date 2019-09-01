sum=lambda arg1,arg2:arg1+arg2

#print(sum(23,17))

s=(lambda a,b:a+b)(11,29)
#print(s)
l=(1,3,7,5,9)
r = filter(lambda i : i>5,l)

for i in r:
    print(i)
print(r)
