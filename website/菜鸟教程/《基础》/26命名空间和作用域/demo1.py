#全局名称
var1 = 5
def sume_func():
    #var2 是局部名称
    var2 = 6
    def some_inner_func():
        #var3 是内嵌的局部名称
        var3 = 7


total = 0
def sum(arg1,arg2):
    total = arg1 + arg2
    print("函数内是局部变量：",total)
    return total

sum(10,20)
print ("函数外是全局变量 : ", total)