#显示系统 的欢迎信息
print('-'*20,'欢迎使用员工管理系统','-'*20)

user_list = []
#user_list.append(['姓名','年龄','性别','住址'])
#根据用户选择做相关的操作
while True:
    #显示 用户的选项
    print("请选择要做的操作：")
    print("\t1.查询员工")
    print("\t2.添加员工")
    print("\t3.删除员工")
    print("\t4.退出系统")
    user_choose = input("请选择【1-4】:")
    if user_choose == '1':
        print('序号\t姓名\t年龄\t性别\t住址')
        k = 0
        for useritem in user_list:
            k += 1
            print(k,end="\t")
            for item in useritem:
                print(item,end="\t")
            print()
        print("\n--------------------------------------")
        
    elif user_choose == '2':
        name = input("请输入员工的姓名：")
        age = input("请输入员工的年龄：")
        sex = input("请输入员工的性别：")
        address = input("请输入员工的住址：")
        print("---------------------------")
        print('姓名\t年龄\t性别\t住址')
        print(name,"\t",age,"\t",sex,"\t",address)
        print("---------------------------")
        isInput = input("是否确认该操作【Y/N】:")
        if isInput == 'Y' or isInput == 'y':
            user_list.append([name,age,sex,address])
            print("添加成功！")
        else:
            print("添加已取消")
            
    elif user_choose =='3':
        user_sort = int(input("请输入要删除的员工的序号："))
        user_key = user_sort-1
        if user_sort > len(user_list):
            print("当前的用户序号不存在")
            continue

        
        print("---------------------------")
        print('序号\t姓名\t年龄\t性别\t住址')
        #print(name,"\t",age,"\t",sex,"\t",address)
        print(user_sort,"\t",user_list[user_key][0],"\t",
              user_list[user_key][1],"\t",user_list[user_key][2],
              "\t",user_list[user_key][3])
        print("---------------------------")
        isInput = input("是否确认该操作【Y/N】:")
        if isInput == 'Y' or isInput == 'y':
            user_list.pop(user_key)
            print("删除成功")
        else:
            print("取消删除")
        
    elif user_choose == '4':
        input("欢迎使用！再见，点击回车键退出")
        break
    else:
        print("您的输入有误，请重新选择！")

print("--------------------------------------")
