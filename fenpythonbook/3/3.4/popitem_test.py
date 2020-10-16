scores={"语文":89,"数学":92,"英语":93}

#popitem 弹出一个元组值
f = scores.popitem()
print(type(f))
k,v  = f
print(k,v)

print(scores)
