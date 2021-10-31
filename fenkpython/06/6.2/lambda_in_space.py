global_fn = lambda p:print("执行lambda表达式,p参数：",p)

class Category:
    cate_fn = lambda p:print("类执行lambda表达式,p参数：",p)

global_fn("fkit")
c = Category()
#自动绑定了self参数 
c.cate_fn()
