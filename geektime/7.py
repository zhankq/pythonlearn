
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

newdata = []
for i in range(3):
    tmp = {}
    for j in range(3):
        tmp[attributes[j]] = values[i][j]
        
    newdata.append(tmp)

#print(newdata)


#for t in values:
#    print(t)

f= [dict(zip(attributes, value)) for value in values]

print(f)

# expected output:
[
{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}
]
