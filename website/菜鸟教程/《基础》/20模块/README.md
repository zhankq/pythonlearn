把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块


import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：

import module1[, module2[,... moduleN]

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

support.py 文件代码
#!/usr/bin/python3
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return
test.py 引入 support 模块：

test.py 文件代码
#!/usr/bin/python3
# Filename: test.py
# 导入模块
import support
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")


一个模块只会被导入一次，不管你执行了多少次import。
这样可以防止导入模块被一遍又一遍地执行。

from … import 语句
from modname import name1[, name2[, ... nameN]]

from … import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
from modname import name1[, name2[, ... nameN]]

>>> from fibo import fib, fib2

from … import * 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *

模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。

每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用


__name__属性

在一个模块（或者脚本，或者其他地方）
的最前面使用 import 来导入一个模块，
当然这只是一个惯例，而不是强制的。

目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，
主要是为了避免一些滥俗的名字（比如叫做 string）
不小心的影响搜索路径中的有效模块。

放一个空的 :file:__init__.py就可以了。
当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） 
__all__变量赋值。



sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py

import sound.effects.echo
from sound.effects.item import iitems

from sound.effects import *
echo.echo_info()
#item.iitems()


无论是隐式的还是显式的相对导入都是从当前模块开始的。
主模块的名字永远是"__main__"，
一个Python应用程序的主模块，应当总是使用绝对路径引用。
