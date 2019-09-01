import time

times = time.localtime(time.time())
timelist = list(times)
needdata = len(timelist)-3
timeformat = timelist[0:3] + [0]*needdata

secs = time.mktime( tuple(timeformat) )
print(secs)


def return_time(day=0):
    nowtime = time.time()-86400*day
    times = time.localtime(nowtime)
    timelist = list(times)
    needdata = len(timelist)-3
    timeformat = timelist[0:3] + [0]*needdata
    return time.mktime( tuple(timeformat))

print(return_time(1))

'''
optSet = {2,'2','f'}


optSet.add(('tuplie','dd'))


optSet.update(['as','job'])
optSet.update({'ads':'PPP','josb':'OOO'})
print(optSet)

optSet.discard('2')


optSet.pop()

print(optSet)




set_1={2,'2','f'}
set_2=set('22f')
f=set('alacazam')
print(f)

'''
