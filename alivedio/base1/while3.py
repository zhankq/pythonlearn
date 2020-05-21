
i = 101

while i <= 999 and i>=101 :
    bai = i // 100
    shi = (i - bai * 100)  // 10
    ge= i % 10

    num = bai ** 3 + shi ** 3 + ge ** 3
    if num == i :
        print(num)

    i += 1

        
