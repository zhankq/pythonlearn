##集合
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
但用set方法只支持
set_1={2,'2','f'}
set_2=set('22f')　＃这一类

将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
optSet = {2,'2','f'}
optSet.add(('tuplie','dd')) #[新增什么就是什么]
#out: {2, 'f', '2', ('tuplie', 'dd')}

#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
optSet.update(['as','job'])
optSet.update({'ads':'PPP','josb':'OOO'})

区别是会拆分成一个个的子元素存入集合中，如果是字典的话存入的是健值
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

3、计算集合元素个数
len(s)


4、清空集合
s.clear()
