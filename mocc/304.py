from pythonds.basic.stack import Stack

#十进制转二进制
def divideBy2(decNumber):
	remstack = Stack()
	while decNumber >0:
		rem = decNumber % 2 #求余数
		remstack.push(rem)#压入栈底
		decNumber = decNumber //2 #整数除

	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString

print(divideBy2(19))
print(divideBy2(17))

#十进制转换为十六进制以下的任意进制
def baseConverter(decNumber,base):
	digits = '0123456789ABCDEF'

	remstack = Stack()
	while decNumber >0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]

	return newString

print(baseConverter(17,2))
print(baseConverter(25,3))
print(baseConverter(25,6))