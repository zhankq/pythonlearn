
def fn(n):
    nums = 1
    for i in range(1,n+1):
        nums *= i
        print(nums,":",i)
    else:
        return nums

f = fn(6)
print(f)