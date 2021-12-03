tour = []
height = []

hei = 100.0
tim = 10

for i in range(10):
    if i == 0:
        tour.append(hei)
    else:
        tour.append(hei*2)
    
    height.append(hei)
    hei /=2

print('总高度:tour={0}'.format(sum(tour)))
print("第10次反弹高度:height = {0}".format(height[-1]))

'''
height=100

for i in range(10):
    height = height/2

print(height)
'''
