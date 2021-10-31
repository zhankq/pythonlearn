def fib1(n):
    f=[1]
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        f.append(a)
    return f


print(fib1(10))



def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
 
# 输出前 10 个斐波那契数列
print (fib(10))