def outputs(s,l):
    if l==0:
        return
    print(s[l-1])
    outputs(s,l-1)

s = input("Input a string:")
l = len(s)
outputs(s,l)
