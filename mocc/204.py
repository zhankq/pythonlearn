'''
解法4，计数比较
其他的参看前面的203
'''

def anagamSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos]+1

    j=0
    stillOK = True
    while j <26 and stillOK:
        if c1[j] == c2[j]:
            j=j+1
        else:
            stillOK = False
    return stillOK

#解法4，用字典的方式计数比较
def anagamSolution5(s1,s2):
    if len(s1)!=len(s2):
        return False
    c1 = dict()
    c2 = dict()
    for i in range(len(s1)):
        if s1[i] in c1:
            c1[s1[i]] += 1
        else:
            c1[s1[i]] = 1
            
        if s2[i] in c2:
            c2[s2[i]] += 1
        else:
            c2[s2[i]] = 1
            
    stillOK = True
    for j in c1:
        if j not in c2 or c1[j]!=c2[j]:
            stillOK = False
            break
        
    return stillOK
            
            
        

#print(anagamSolution4("apple","pleap"))

print(anagamSolution5("appless","splseap"))
