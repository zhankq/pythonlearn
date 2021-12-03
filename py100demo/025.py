s = 0
jiechen_no = 4
for i in range(1,jiechen_no+1):
    k=1
    for j in range(1,(i+1)):
        k *= j
    print(k)
    s+=k
print("====")        
print(s)



n = 0
s = 0
t = 1
for n in range(1,5):
    t *= n
    s += t

print(s)
