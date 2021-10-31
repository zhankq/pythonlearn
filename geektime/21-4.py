'''
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


def func1():
    show_memory_info('initial')
    a = [i for i in range(100000)]
    b = [i for i in range(100000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func1()
gc.collect()
show_memory_info('finished')

'''

import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

#objgraph.show_backrefs([a])
objgraph.show_refs([a])