stack = []
#向栈中入栈3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")

print(stack)
#第一出栈：最后的入栈的出去
print(stack.pop())
print(stack)
#再次出栈
print(stack.pop())
print(stack)

'''
stack = []
#向栈中加3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack)
#第一次出栈，最后的元素被移除
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
'''