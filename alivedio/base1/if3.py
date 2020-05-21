dog_age = int(input("请输入狗的年龄："))

base_user_age = 10.5

if dog_age <=2 :
    print("相当于人类的年龄：",base_user_age*2)
else:
    base_user_age = base_user_age*2+(dog_age-2)*4
    print("相当于人类年龄：",base_user_age)
    
