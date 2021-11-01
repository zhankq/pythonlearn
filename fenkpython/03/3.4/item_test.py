#items()
scores={"语文":89,"数学":92,"英语":93}
ims = scores.items()
print(list(ims))
#keys()
kys = scores.keys()
print(list(kys)[0])

tuplekys = tuple(kys)
print("tuples:",tuplekys)

#vvalues()
vals = scores.values()
print(list(vals)[0])
