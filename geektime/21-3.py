import gc
import os
import psutil

#显示 当前python程序占用的内存
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{} memory used: {} MB'.format(hint,memory))

a= [i for i in range(1000000)]

show_memory_info('after a created')

del a
gc.collect()
show_memory_info('finished')

# print(a)