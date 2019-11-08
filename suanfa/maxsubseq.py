#最大子序列之和，从左往右进行
def MaxSubseqSum1(A):
    ThisSum = MaxSum = 0
    N=len(A)
    for i in range(N):
        for j in range(i,N):
            ThisSum=0
            for k in range(i,j+1):
                ThisSum+=A[k];
            if (ThisSum>MaxSum) :
                MaxSum = ThisSum

    return MaxSum

s = MaxSubseqSum1([1,2,4,4,5,-10])
print(s)

def MaxSubseqSum4(A):
    N=len(A)
    ThisSum = MaxSum = 0
    for i in range(N):
        ThisSum+=A[i]
        if(ThisSum>MaxSum):
            MaxSum=ThisSum
        elif (ThisSum<0):
            ThisSum=0
    return MaxSum

s = MaxSubseqSum4([1,-4,2,4,4,5,-10,54])
print(s)

