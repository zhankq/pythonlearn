'''
n=int(input())
def fbnq(n):
    f1,f2=0,1
    for i in range(n):
	    f1,f2=f2,f1+f2
    return f1
	
print(fbnq(n))
'''
for i in range(1,4):
    print(i)
	
	
num1 = int(input(""))
num2 = int(input(""))
def hcf(n1,n2):
    for i in range(min(n1,n2),0,-1):
	    if n1 % i== n2 % i ==0:
		    return i
print(hcf(num1,num2))