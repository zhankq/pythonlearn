from pythonds.stackop import Stack
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(43,2))

print(baseConverter(43,8))
print(baseConverter(43,16))
