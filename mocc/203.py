def anagramSolution1(s1,s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1<len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1
    return stillOK

print(anagramSolution1("abcd","cdba"))

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos<len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            maches = False
    return matches

print(anagramSolution2("asbcd","scdba"))


def author_anagramSolution(s1,s2):
    found = True
    for i in s1:
        if i not in s2:
            found = False
            break
    return found

print(author_anagramSolution("asbcdw","scdba"))

