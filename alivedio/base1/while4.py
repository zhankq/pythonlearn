'''
while True:
    num = int(input("判断这是否是质数："))

    if num == 1 :
        print("什么都不是")
        break
    j = 3
    while j >2 and j < num:
        if num % j == 0 :
            print("不为质数,请继续")
            j += 1
            break
        j+=1
    else:
        print("是质数")
        break
''' 


