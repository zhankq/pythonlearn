x2 = 1
for day in range(9):
    x1 = (x2+1)*2 # 前一天的量
    x2 = x1
    
print(x1)
