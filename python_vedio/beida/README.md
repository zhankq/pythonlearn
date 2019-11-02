列表推导式
[<表达式> for <变量> in <可迭代对象> if <逻辑条件>]

字典推导式

{<键值表达式>:<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>}

集合推导式
{<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>}



与推导式一样语法：

(<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>)

agen = (x*x for x in range(10))
>>> agen
<generator object <genexpr> at 0x00000212C4D8BCF0>
>>> for n in agen:
	print(n)

