scores = {"语文":89,"数学":92,"英语":93}
print(scores)
empty_dict = {}
print(empty_dict)
#使用元组做dict的key
dict2 = {(20,30):"good",30:"bad"}
print(dict2)

vegetables = [("celery",1.58),("brocoli",1.29),('lettuce',2.19)]
#创建包含3个k-v对的字典
dict3 = dict(vegetables)
print(dict3)
cars = [["bmw",8.5],("a",44)]
dict4 = dict(cars)
print(dict4)
empty_dict = dict()
print(empty_dict)
#使用关键字参数来创建字典
dict6 = dict(sp=1.69,cab=33)
print(dict6)