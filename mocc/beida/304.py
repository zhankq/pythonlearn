from pythonds.stackop import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2 #取余数
        remstack.push(rem)
        decNumber = decNumber //2 #整除部分

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(43))
