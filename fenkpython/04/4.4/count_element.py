#统计各元素出现的次数
src_list = [12,45,3.4,12,"fkit",45,3.4,"fkit",45,3.4]
statistis = {}
for ele in src_list:
	#如果字典中包含ele代表的key
	if ele in statistis:
		statistis[ele] += 1
	else:
		statistis[ele] = 1

for ele,count in statistis.items():
	print("%s 出现的次数为：%d" % (ele,count))