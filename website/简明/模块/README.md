##模块

编写模块有很多种方法，其中最简单的一种便是创建一个包含函数与变量、以 .py 为后缀的文件。
另一种方法是使用撰写 Python 解释器本身的本地语言来编写模块。举例来说，
你可以使用 C 语言来撰写 Python 模块，并且在编译后，你可以通过标准 Python 解释器在你的 Python 代码中使用它们。


编写你自己的模块

编写你自己的模块很简单，这其实就是你一直在做的事情！这是因为每一个 Python 程序同时也是一个模块。
你只需要保证它以 .py 为扩展名即可。下面的案例会作出清晰的解释。

案例（保存为 mymodule.py）：
def say_hi():
    print('Hi, this is mymodule speaking.')

__version__ = '0.1'
上方所呈现的就是一个简单的模块。正如你所看见的，与我们一般所使用的 Python 的程序相比其实并没有什么特殊的区别。我们接下来将看到如何在其它 Python 程序中使用这一模块。
要记住该模块应该放置于与其它我们即将导入这一模块的程序相同的目录下，或者是放置在 sys.path 所列出的其中一个目录下。
另一个模块（保存为 mymodule_demo.py）：
import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)


警告：要记住你应该避免使用 import 这种形式，即 `from mymodule import `。
Python 之禅
Python 的一大指导原则是“明了胜过晦涩”2。你可以通过在 Python 中运行 import this 来了解更多内容。


内置的 dir() 函数能够返回由对象所定义的名称列表。
如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。
