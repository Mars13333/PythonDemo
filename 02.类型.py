
# 数字
17 / 3  # 经典除法运算返回一个浮点数
5.666666666666667

17 // 3  # 向下取整除法运算会丢弃小数部分
5

17 % 3  # % 运算返回相除的余数
2

5 * 3 + 2  # 向下取整的商 * 除数 + 余数
17

5 ** 2  # 5 的平方
25

2 ** 7  # 2 的 7 次方
128

# Python 全面支持浮点数；混合类型运算数的运算会把整数转换为浮点数：
4 * 3.75 - 1
14.0

# 除了 int 和 float，Python 还支持其他数字类型，例如 Decimal 或 Fraction。Python 还内置支持 复数，后缀 j 或 J 用于表示虚数（例如 3+5j ）。


#------------------------------------------------------------------------

# 文本

'spam eggs'  # single quotes
"Paris rabbit got your back :)! Yay!"  # double quotes
'1975'  # digits and numerals enclosed in quotes are also strings


# 要标示引号本身，我们需要对它进行“转义”，即在前面加一个 \。 或者，我们也可以使用不同类型的引号:
'doesn\'t'  # 使用 \' 来转义单引号...
"doesn't"
"doesn't"  # ...或者改用双引号
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'

# 在 Python shell 中，字符串定义和输出字符串看起来可能不同。 print() 函数会略去标示用的引号，并打印经过转义的特殊字符，产生更为易读的输出:
s = 'First line.\nSecond line.'  # \n 表示换行符
s  # 不用 print()，特殊字符将包括在字符串中
'First line.\nSecond line.'
print(s)  # 用 print()，特殊字符会被转写，因此 \n 将产生一个新行
'First line.'
'Second line.'


# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可：
print('C:\some\name')  # 这里 \n 表示换行符！
'C:\some'
'ame'
print(r'C:\some\name')  # 请注意引号前的 r
'C:\some\name'


# 字符串文字可以跨越多行。一种方法是使用三重引号："""...""" 或 '''...''' 。
# 行尾会自动包含在字符串中，但可以通过在行尾添加 \ 来避免这种情况。


# 字符串可以用 + 合并（粘到一起），也可以用 * 重复：
# 3 乘以 'un'，再加 'ium'
3 * 'un' + 'ium'
'unununium'

# 这项功能只能用于两个字面值，不能用于变量或表达式!
# 合并多个变量，或合并变量与字面值，要用 +：
prefix = 'py'
prefix + 'thon'
'Python'


# 字符串支持 索引 （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：
word = 'Python'
word[0]  # 0 号位的字符
'P'
word[5]  # 5 号位的字符
'n'


# 索引还支持负数，用负数索引时，从右边开始计数：
word[-1]  # 最后一个字符
'n'
word[-2]  # 倒数第二个字符
'o'
word[-6]
'P'

# 注意，-0 和 0 一样，因此，负数索引从 -1 开始。
# 除了索引操作，还支持 切片。 索引用来获取单个字符，而 切片 允许你获取子字符串:
word[0:2]  # 从 0 号位 (含) 到 2 号位 (不含) 的字符
'Py'
word[2:5]  # 从 2 号位 (含) 到 5 号位 (不含) 的字符
'tho'


# 切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：
word[:2]   # 从开头到 2 号位 (不含) 的字符
'Py'
word[4:]   # 从 4 号位 (含) 到末尾
'on'
word[-2:]  # 从倒数第二个 (含) 到末尾
'on'

# 注意，输出结果包含切片开始，但不包含切片结束。因此，s[:i] + s[i:] 总是等于 s：
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'


# 还可以这样理解切片，索引指向的是字符 之间 ，第一个字符的左侧标为 0，最后一个字符的右侧标为 n ，n 是字符串长度。例如：
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


# 索引越界会报错：
word[42]  # word 只有 6 个字符
'Traceback (most recent call last):'
'File "<stdin>", line 1, in <module>'
'IndexError: string index out of range'

# 但是，切片会自动处理越界索引：
word[4:42]
'on'
word[42:]
''

# Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错：
# 要生成不同的字符串，应新建一个字符串：
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'

# 内置函数 len() 返回字符串的长度：
s = 'supercalifragilisticexpialidocious'
len(s)
34




#------------------------------------------------------------------------


# 列表

# Python 支持多种 复合 数据类型，可将不同值组合在一起。最常用的 列表 ，是用方括号标注，逗号分隔的一组值。
# 列表 可以包含不同类型的元素，但一般情况下，各个元素的类型相同：
squares = [1, 4, 9, 16, 25]


# 和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片：
squares[0]  # 索引操作将返回条目
1
squares[-1]
25
squares[-3:]  # 切片操作将返回一个新列表
[9, 16, 25]

# 列表还支持合并操作：
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 与 immutable 字符串不同, 列表是 mutable 类型，其内容可以改变：
cubes = [1, 8, 27, 65, 125]  # 这里有点问题
4 ** 3  # 4 的立方是 64，不是 65！
64
cubes[3] = 64  # 替换错误的值
cubes
[1, 8, 27, 64, 125]


# 你也可以在通过使用 list.append() 方法，在列表末尾添加新条目:
cubes.append(216)  # 添加 6 的立方
cubes.append(7 ** 3)  # 和 7 的立方
cubes
[1, 8, 27, 64, 125, 216, 343]


# Python 中的 简单赋值 绝不会复制数据。 当你将一个列表赋值给一个变量时，该变量将引用 现有的列表。
# 你通过一个变量对列表所做的任何更改都会被引用它的所有其他变量看到。:
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # 它们指向同一个对象
True
rgba.append("Alph")
rgb
["Red", "Green", "Blue", "Alph"]


# 切片操作 返回包含请求元素的 新列表。以下切片操作会返回列表的 浅拷贝：
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba
["Red", "Green", "Blue", "Alpha"]
rgba
["Red", "Green", "Blue", "Alph"]


# 为切片赋值可以改变列表大小，甚至清空整个列表：
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 替换一些值
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# 现在移除它们
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# 通过用一个空列表替代所有元素来清空列表
letters[:] = []
letters
[]

# 内置函数 len() 也支持列表：
letters = ['a', 'b', 'c', 'd']
len(letters)
4

# 还可以嵌套列表（创建包含其他列表的列表），例如：
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'
