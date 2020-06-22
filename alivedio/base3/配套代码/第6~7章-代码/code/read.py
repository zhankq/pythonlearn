# try:
# 	filecontent = ""
# 	with open("demo.txt") as fileobj:
# 		readcount = 100
# 		while True:
# 			content = fileobj.read(readcount)
# 			filecontent += content
# 			if not content:
# 				break
# except:
# 	print("over")

# print(filecontent)
# try:
# 	with open("demo.txt") as fileobj:
# 		for t in fileobj:
# 			print(t)
# except:
# 	print("error")

# try:
# 	with open("demo.txt") as fileobj:
# 		lines = fileobj.readlines()
# 		# print(lines)
# 		for line in lines:
# 			print(line)
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass

with open("demo.txt") as fileobj:
	while True:
		line = fileobj.readline()
		if not line:
			break
		print(line)