scores={"语文":89,"数学":92,"英语":93}
print(scores)
f={1,2} #集合
print(type(f))
#空的花括号代表空的 dict
empty_dict={}
#使用无组作为dict的key
print(empty_dict)
dict2= {(20,30):"good",30:"bad"}
print(dict2[(20,30)])

vegetables = [("celery",1.56),("brocoli",1.29),("lettuce",2.19)]
#创建包含3个key-value 的字典
dict3 = dict(vegetables)
print(dict3)
vegetablelst = [["celery",1.56],["brocoli",1.29],["lettuce",2.19]]
dict4 = dict(vegetablelst)
print(dict4)
dict5 = dict()
print(dict5==empty_dict) #true
#使用关键词来创建
dict6=dict(spinach=1.39,cabbage=2.59)
print(dict6["spinach"])





