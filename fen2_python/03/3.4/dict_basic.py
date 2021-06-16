scores = {"语文":89}
print(scores['语文'])
scores['数学'] = "93"
scores[92] = 5.7
print(scores)

del scores["语文"]
del scores['数学'] 
print(scores)

cars = {"bmw":8.5,"bens":8.3,"audi":9.9}
print(cars)
cars["bmw"] = 4.4
cars["bens"] = 4.4
print(cars)
#in 或 not in 是基于key判断 的

print("bmw" in cars)

print("bmwd" not in cars)