# encoding=UTF-8
#你能够引发的错误或异常必须是直接或间接从属于 Exception（异常） 类的派生类。
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
    #其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
#'''
#在 except 子句中，我们提及了错误类，将该类存储 as（为） 相应的错误名或异常名。
#这类似于函数调用中的形参与实参。
#在这个特殊的 except 子句中我们使用异常对象的 length 与 atleast 字段来向用户打印一条合适的信息
#'''
except ShortInputException as ex:
    print(('ShortInputException:The input was {0} long, expected at least {1}').format(ex.length,ex.atleast))
else:
    print('No exception was raised')
