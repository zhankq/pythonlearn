多行语句

	Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：

	total = item_one + \
	        item_two + \
	        item_three

	在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：

	total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
