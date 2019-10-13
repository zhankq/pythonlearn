try ... except 语句可以带有一个 else子句，该子句只能出现在所有 except 子句之后。当 try 语句没有抛出异
常时，需要执行一些代码，可以使用这个子句

在异常名（列表）之后，也可以为 except 子句指定一个变量。这个变量绑定于一个异常实例，它存储在
instance.args 的参数中。为了方便起见，异常实例定义了 __str__() ，
这样就可以直接访问过打印参数而不
必引用 .args 。这种做法不受鼓励。相反，更好的做法是给异常传递一个参数（如果要传递多个参数，可
以传递一个元组），把它绑定到 message 属性

>>> try:
... raise Exception('spam', 'eggs')
... except Exception as inst:
... print(type(inst)) # the exception instance
... print(inst.args) # arguments stored in .args
... print(inst) # __str__ allows args to be printed directly,
... # but may be overridden in exception subclasses
... x, y = inst.args # unpack args
... print('x =', x)
... print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs


如果一个新创建的模块中需要抛出几种不同的错误时，
一个通常的作法是为该模
块定义一个异常基类，然后针对不同的错误类型派生出对应的异常子类


class Error(Exception):
"""Base class for exceptions in this module."""
pass
class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
    expression ‐‐ input expression in which the error occurred
    message ‐‐ explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.
    Attributes:
    previous ‐‐ state at beginning of transition
    next ‐‐ attempted new state
    message ‐‐ explanation of why the specific transition is not allowed
    """
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


与标准异常相似，大多数异常的命名都以 “Error” 结尾。


不管有没有发生异常，finally子句 在程序离开 try 后都一定会被执行。
当 try 语句中发生了未被 except 捕获
的异常（或者它发生在 except 或 else 子句中），
在 finally 子句执行完后它会被重新抛出。 try 语句经由
break ，continue 或 return 语句退 出也一样会执行 finally 子句。


8.7. 预定义清理
这段代码的问题在于在代码执行完后没有立即关闭打开的文件。这在简单的脚本里没什么，但是大型应用
程序就会出问题。with 语句使得文件之类的对象可以 确保总能及时准确地进行清理。
with open("myfile.txt") as f:
    for line in f:
        print(line)

语句执行后，文件 f 总会被关闭，即使是在处理文件中的数据时出错也一样。
其它对象是否提供了预定义的
清理行为要查看它们的文档
