from pythonds.basic.stack import Stack

#括号匹配算法
def parChecker(symbolString):
	s = Stack()
	balanced = True #查找是否匹配
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
				break
			else:
				s.pop()

		index = index + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

print(parChecker("((()))"))
print(parChecker("((())"))
