scores={"语文":89,"数学":92,"英语":93}
#总能返回指定的值，如果不存在则设置一个值
#例 a 不存在，则返回 a 的值 并设置了一个 a元素
f = scores.setdefault("a","f")
print(f)
print(scores)

#例 英语 存在，则返回 英语 的值  设置的一个 元素值 f 则无效

f = scores.setdefault("英语","f")
print(f)


print(scores)
