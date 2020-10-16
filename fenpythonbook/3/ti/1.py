s = input("输入多个字串,分隔：")

tuples = s.split(',')
tuple_input = tuple(tuples)

print(tuple_input*3)

print(tuple_input+("fkjava","crazyit"))
