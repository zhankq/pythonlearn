
序列
列表、元组和字符串可以看作序列（Sequence）的某种表现形式，可是究竟什么是序列，它又有什么特别之处？
序列的主要功能是资格测试（Membership Test）（也就是 in 与 not in 表达式）和索引操作（Indexing Operations），它们能够允许我们直接获取序列中的特定项目。
上面所提到的序列的三种形态——列表、元组与字符串，同样拥有一种切片（Slicing）运算符，它能够允许我们序列中的某段切片——也就是序列之中的一部分

>#列表del一个元素后内容索引会被重置，重新从0开始计数

要注意的是切片操作会在开始处返回 start，并在 end 前面的位置结束工作。
也就是说，序列切片将包括起始位置，但不包括结束位置。

你会注意到当步长为 2 时，我们得到的是第 0、2、4…… 位项目。当步长为 3 时，我们得到的是第 0、3……位项目。


issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
bri = set(['brazil', 'russia', 'india'])
bric = bri.copy()
bric.issuperset(bri)  #返回 true

你要记住如果你希望创建一份诸如序列等复杂对象的副本
（而非整数这种简单的对象（Object）），
你必须使用切片操作来制作副本。【注：或是类似.copy】
如果你仅仅是将一个变量名赋予给另一个名称，
那么它们都将“查阅”同一个对象，
如果你对此不够小心，那么它将造成麻烦。

