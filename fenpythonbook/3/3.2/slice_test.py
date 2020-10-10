a_tuple=('crazyit',20,5.6,'fkit',-17)
#第2个到第4个【不包含】的所有元素
print(a_tuple[1:3])
#倒数第3到倒数第1个【不包含】的所有元素
print(a_tuple[-3:-1])#5.6,'fkit'
#倒数第3到第5个【不包含】的所有元素
print(a_tuple[-3:4])#5.6,'fkit'
#带step
b_tuple=(1,2,3,4,5,6,7,8,9)
#第3到第9间隔为2的元素
print(b_tuple[2:8:2])#3,5,7

print(b_tuple[2:8:3])#3,6
#第3到倒数第2间隔为2
print(b_tuple[2:-2:2])#3，5，7
