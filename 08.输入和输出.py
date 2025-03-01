# 输入与输出

'''
程序输出有几种显示方式；数据既可以输出供人阅读的形式，也可以写入文件备用。
'''

## 更复杂的输出

'''
到目前为止我们已遇到过两种写入值的方式: 表达式语句 和 print() 函数。第三种方式是使用文件对象的 write() 方法；
标准输出文件可以被引用为 sys.stdout。 

对输出格式的控制不只是打印空格分隔的值，还需要更多方式。格式化输出包括以下几种方法。

使用 格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。
在这种字符串中，可以在 { 和 } 字符之间输入引用的变量，或字面值的 Python 表达式。
'''

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
'Results of the 2016 Referendum'

'''
字符串的 str.format() 方法需要更多手动操作。 你仍将使用 { 和 } 来标记变量将被替换的位置并且可以提供详细的格式化指令，
但你还需要提供待格式化的信息。 下面的代码块中有两个格式化变量的例子：
'''
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'

'''
请注意Notice how the yes_votes 填充了空格并且只为负数添加了负号。 
这个例子还打印了 percentage 乘以 100 的结果，保留 2 个数位并带有一个百分号 (请参阅 格式规格迷你语言 了解详情)。

最后，还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。
字符串类型还支持将字符串按给定列宽进行填充，这些方法也很有用。

如果不需要花哨的输出，只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串。

str() 函数返回供人阅读的值，repr() 则生成适于解释器读取的值（如果没有等效的语法，则强制执行 SyntaxError）。
对于没有支持供人阅读展示结果的对象， str() 返回与 repr() 相同的值。一般情况下，数字、列表或字典等结构的值，
使用这两个函数输出的表现形式是一样的。字符串有两种不同的表现形式。
'''

### 格式化字符串字面值

'''
格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，
把 Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。下例将 pi 舍入到小数点后三位：
'''
import math

print(f'The value of pi is approximately {math.pi:.3f}.')
'The value of pi is approximately 3.142.'

'''
在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐：
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

'Sjoerd     ==>       4127'
'Jack       ==>       4098'
'Dcab       ==>       7678'


'= 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。'
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
"Debugging bugs='roaches' count=13 area='living room'"


### 字符串format()方法

'str.format() 方法的基本用法如下所示：'
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
'We are the knights who say "Ni!"'


'''
花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。
花括号中的数字表示传递给 str.format() 方法的对象所在的位置。
'''
print('{0} and {1}'.format('spam', 'eggs'))
'spam and eggs'
print('{1} and {0}'.format('spam', 'eggs'))
'eggs and spam'


'str.format() 方法中使用关键字参数名引用值。'
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
'This spam is absolutely horrible.'


'位置参数和关键字参数可以任意组合：'
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
'The story of Bill, Manfred, and Georg.'

'''
如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。
这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成。
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098
Sjoerd: 4127
Dcab: 8637678

'''
{0}表示引用第一个参数（即table字典），后续通过键名（如Jack）访问对应的值.
{0[Jack]:d}：0指向table字典，Jack是键名，:d指定将值格式化为十进制整数。
字符串中所有占位符均通过{0[key]}引用同一个字典table，避免重复传参.

这也可以通过将 table 字典作为采用 ** 标记的关键字参数传入来实现。
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098
Sjoerd: 4127
Dcab: 8637678

'''
与内置函数 vars() 一同使用时这种方式非常实用，它将返回一个包含所有局部变量的字典:
'''
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k + '};' for k in table.keys()])
print(message.format(**table))
'''
__name__: __main__
__doc__: None
__package__: None
__loader__: ...
'''

'举个例子，以下几行代码将产生一组整齐的数据列，包含给定的整数及其平方与立方:'
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

{0:2d}：第一个占位符（对应x），格式化为宽度为2的十进制整数。不足2位时右对齐，左侧补空格。
{1:3d}：第二个占位符（对应平方值），宽度为3。
{2:4d}：第三个占位符（对应立方值），宽度为4
'''

## 读写文件

'''
open() 返回一个 file object ，最常使用的是两个位置参数和一个关键字参数：open(filename, mode, encoding=None)
第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。
mode 的值包括 'r' ，表示文件只能读取；
'w' 表示只能写入（现有同名文件会被覆盖）；
'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。
'r+' 表示打开文件进行读写。
mode 实参是可选的，省略时的默认值为 'r'。
'''
f = open('workfile', 'w', encoding="utf-8")


'''
通常情况下，文件是以 text mode 打开的，也就是说，你从文件中读写字符串，这些字符串是以特定的 encoding 编码的。
如果没有指定 encoding ，默认的是与平台有关的（见 open() ）。
因为 UTF-8 是现代事实上的标准，除非你知道你需要使用一个不同的编码，否则建议使用 encoding="utf-8" 。
在模式后面加上一个 'b' ，可以用 binary mode 打开文件。二进制模式的数据是以 bytes 对象的形式读写的。
在二进制模式下打开文件时，你不能指定 encoding 。

在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。
而且，使用 with 相比等效的 try-finally 代码块要简短得多：
'''
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# 我们可以检测文件是否已被自动关闭。
f.closed
True

'''
如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源。

警告 调用 f.write() 时，未使用 with 关键字，或未调用 f.close()，
即使程序正常退出，也**可能** 导致 f.write() 的参数没有完全写入磁盘。
通过 with 语句，或调用 f.close() 关闭文件对象后，再次使用该文件对象将会失败。
'''
f.close()
f.read()
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
'''

### 文件对象的方法

'''
本节下文中的例子假定已创建 f 文件对象。

f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。 
size 是可选的数值参数。省略 size 或 size 为负数时，读取并返回整个文件的内容；文件大小是内存的两倍时，会出现问题。
size 取其他值时，读取并返回最多 size 个字符（文本模式）或 size 个字节（二进制模式）。
如已到达文件末尾，f.read() 返回空字符串（''）。
'''
f.read()
'This is the entire file.\n'
f.read()
''

'''
f.readline() 从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。
这种方式让返回值清晰明确；只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，空行使用 '\n' 表示，
该字符串只包含一个换行符。
'''
f.readline()
'This is the first line of the file.\n'
f.readline()
'Second line of the file\n'
f.readline()
''


'''
从文件中读取多行时，可以用循环遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单：
'''
for line in f:
    print(line, end='')

'This is the first line of the file.'
'Second line of the file'

'''
如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()。

f.write(string) 把 string 的内容写入文件，并返回写入的字符数。

'''
f.write('This is a test\n')
15

'写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）：'
value = ('the answer', 42)
s = str(value)  # 将元组转换为字符串
f.write(s)
18

'''
f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字。

f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；
参考点由 whence 参数指定。 whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。
省略 whence 时，其默认值为 0，即使用文件开头作为参考点。

'''
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
16
f.seek(5)  # 定位到文件中的第 6 个字节
5
f.read(1)
b'5'
f.seek(-3, 2)  # 定位到倒数第 3 个字节
13
f.read(1)
b'd'

'''
在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2) 搜索到文件末尾是个例外），
唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为。

'''

### 使用json保存结构化数据

'''
字符串可以很容易地写入文件或从文件中读取。 数字则更麻烦一些，因为 read() 方法只返回字符串，
而字符串必须传给 int() 这样的函数，它接受 '123' 这样的字符串并返回其数值 123。 
当你想要保存嵌套列表和字典等更复杂的数据类型时，手动执行解析和序列化操作将会变得非常复杂。

Python 允许你使用流行的数据交换格式 JSON (JavaScript Object Notation)，
而不是让用户持续编写和调试代码来将复杂的数据类型存入文件中。 
标准库模块 json 可以接受带有层级结构的 Python 数据，并将其转换为字符串表示形式；这个过程称为 serializing。 
根据字符串表示形式重建数据则称为 deserializing。 在序列化和反序列化之间，用于代表对象的字符串可以存储在文件或数据库中，
或者通过网络连接发送到远端主机。

只需一行简单的代码即可查看某个对象的 JSON 字符串表现形式：
'''
import json

x = [1, 'simple', 'list']
json.dumps(x)
'[1, "simple", "list"]'


'''
dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file 。因此，如果 f 是 text file 对象，可以这样做：
'''
json.dump(x, f)
'要再次解码对象，如果 f 是已打开、供读取的 binary file 或 text file 对象：'
x = json.load(f)
