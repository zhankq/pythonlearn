def fn(n):
    total = n*n
    totals = []
    j = []
    for i in range(1,total+1):
        print(i,end=" ")
        j.append(i)
        if i % n == 0:
            print()
            totals.append(j)
            j=[]
            
    print("------------")
    print(totals)
    for i in range(n):#行
        for j in range(n):#列
            print(totals[j][i],end=" ")
        print()



fn(3)