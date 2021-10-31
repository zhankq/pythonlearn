#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

###扩展###取出无重复的，即【1,2,3】 这种与 【2，1，3】是一样的去掉
a = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k and i!=j and j!=k):
                print(i,j,k)
                tmp = sorted([i,j,k])
                if( tmp not in a):
                    a.append(tmp)

print("不重复的",a)
