#幂运算
'''
def power(n,i):
    if i==1:
        return n
    else:
        return n*(power(n,(i-1)))

nums = power(2,10)
print(nums)
'''

#回字符串
def huiwen(strs):
    if len(strs)<2:
        return True
    elif strs[0]!=strs[-1]:
        return False
    return huiwen(strs[1:-1])#取出了中间的部分

f=huiwen('cpaapc')
print(f)
