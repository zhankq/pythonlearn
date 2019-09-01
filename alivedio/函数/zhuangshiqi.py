#装饰器函数

def begin_end(old):
    def new_function(*args,**kwargs):
        print("开始执行~~~~")

        result= old(*args,**kwargs)

        print("执行结束")
        return result
    return new_function

#当前的函数被装饰了
@begin_end
def say_hello():
    print("大家好")

say_hello()
