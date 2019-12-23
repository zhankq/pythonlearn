import sys
def shuang(a,b):
    if not isinstance(a, int):
        raise Exception('除数 {} 不为整数'.format(a))

    if not isinstance(b,int):
        raise Exception('被除数 {} 不为整数'.format(b))

    return_val = 1
    while (return_val < 10):
        yield return_val;
        return_val = a/b 


a = int(input('请输入除数:'))
b = int(input('请输入被除数:'))


try:
    for i in shuang(a,b):
        print(i)
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()
finally:
    sys.exit('finally')