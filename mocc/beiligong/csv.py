#fo = open('csv.txt')
fo = open('ls.csv','r', encoding='UTF-8')
ls = []


for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()
for l in ls :
    print(l)

#ls2 = [[],[]]
f2 = open('ls2.csv','w')
for item in ls:
    f2.write(','.join(item)+'\n')
f2.close()
