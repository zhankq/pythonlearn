#简单生成器
'''
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested=[[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)

print(list(flatten(nested)))
'''
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

s = list(flatten([[[1],2],3,4,[5,[6,7]],8]))
print(s)
