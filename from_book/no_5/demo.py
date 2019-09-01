import sys

from math import sqrt

scope={}
exec('sqrt=1',scope)

sqrt(4)


s={"a":"222","b":"good"}

rob = s

#print(rob)
#print(s)
s=None
print(rob)

print(s)


sys.exit('')

index=0
strings="good job , well done"
for index,string in enumerate(strings):
    print(index,"|"
                ""
                "",string)
    if 'job' in string:
        strings[index]= "[censored]"

print(strings)


names =["anne","beth","george","damon"]
ages= [12,45,32,10]
for name,age in zip(names,ages):
    print(name,age)

dicts = {'a':11,'b':22,'c':33}

print(dicts.items())
for k,v in dicts.items():
    print(k,'_',v)

for v in dicts.values():
    print(v)


sys.exit('');

lst = [1,2,'aa','bb']
for i in lst:
    print(i)



x,y=(1,4)
print(x,y)


s={"name":'wjc123',"age":"45"}

key,val=s.popitem()

print(' '.isspace())
