age = 45
if age > 60:
	print("老年人")
if age > 40 and not (age > 60):
	print("中年人")
if age>20 and not(age>60) and not(age>40 and not(age>60)):
	print("青年人")