height = int(input("身高："))
money = int(input("金额："))
suai = int(input("帅度："))

if height >= 180 and money >= 1000 and suai >=0:
    print("must do")
elif height >= 180 or money >= 1000 or suai >=0:
    print("ok ?")
else:
    print("no")
