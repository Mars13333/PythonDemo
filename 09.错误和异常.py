# 错误和异常

'''
至此，本教程还未深入介绍错误信息，但如果您尝试过本教程前文中的例子，应该已经看到过一些错误信息。
错误可（至少）被分为两种：语法错误 和 异常。
'''

## 语法错误

'''
语法错误又称 解析错误，是学习 Python 时最常见的错误：
'''
while True print('Hello world') # type:ignore
  '''File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax'''

'''
解析器会重复存在错误的行并显示一个指向廖行中检测到错误的词元的小箭头。 
错误可能是由于所指向的词元 之前 缺少某个词元而导致的。 
在这个例子中，错误是在函数 print() 上检测到的，原因是在它之前缺少一个冒号 (':')。 
文件名和行号也会被打印出来以便你在输入是来自脚本时可以知道要去哪里查找问题。
'''


## 异常

'''
即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 异常，
异常不一定导致严重的后果：很快我们就能学会如何处理 Python 的异常。大多数异常不会被程序处理，而是显示下列错误信息：
'''
10 * (1/0)
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero'''
4 + spam*3
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined'''
'2' + 2
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str'''

## 异常的处理

'''
可以编写程序处理选定的异常。下例会要求用户一直输入内容，直到输入有效的整数，
但允许用户中断程序（使用 Control-C 或操作系统支持的其他操作）；注意，用户中断程序会触发 KeyboardInterrupt 异常。
'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

'''
首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。

如果没有触发异常，则跳过 except 子句，try 语句执行完毕。

如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 
如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，
然后跳到 try/except 代码块之后继续执行。

如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外层的 try 语句中；
如果没有找到处理器，则它是一个 未处理异常 且执行将停止并输出一条错误消息。


try 语句可以有多个 except 子句 来为不同的异常指定处理程序。 但最多只有一个处理程序会被执行。 
处理程序只处理对应的 try 子句 中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。 
except 子句 可以用带圆括号的元组来指定多个异常，例如:
except (RuntimeError, TypeError, NameError):
     pass
     

except 子句 可能会在异常名称后面指定一个变量。 这个变量将被绑定到异常实例，该实例通常会有一个存储参数的 args 属性。 
为了方便起见，内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args。
'''
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # 异常的类型
    print(inst.args)     # 参数保存在 .args 中
    print(inst)          # __str__ 允许 args 被直接打印，
                         # 但可能在异常子类中被覆盖
    x, y = inst.args     # 解包 args
    print('x =', x)
    print('y =', y)

<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

'''
Exception 可以被用作通配符，捕获（几乎）一切。然而，好的做法是，尽可能具体地说明我们打算处理的异常类型，
并允许任何意外的异常传播下去。
'''

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


'''
try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。 
它适用于 try 子句 没有引发异常但又必须要执行的代码。 例如:
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


## 触发异常

'raise 语句支持强制触发指定的异常。例如：'

raise NameError('HiThere')
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere'''


'''
raise 唯一的参数就是要触发的异常。这个参数必须是异常实例或异常类（派生自 BaseException 类，例如 Exception 或其子类）。
如果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化：

raise ValueError  # 'raise ValueError()' 的简化

如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异常：
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
'''
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere

执行 raise，重新抛出被捕获的异常（NameError）。
最终，程序会因为未被处理的异常而崩溃
如果没有 raise，异常将被抑制，程序继续执行：
'''



## 异常链

'如果一个未处理的异常发生在 except 部分内，它将会有被处理的异常附加到它上面，并包括在错误信息中:'
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

'''Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error'''


'''
为了表明一个异常是另一个异常的直接后果， raise 语句允许一个可选的 from 子句:

'''
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

'''Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database'''


'''
它还允许使用 from None 表达禁用自动异常链:
'''
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

'''Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError'''


## 用户自定义异常

'''
程序可以通过创建新的异常类命名自己的异常,不论是以直接还是间接的方式，异常都应从 Exception 类派生。

异常类可以被定义成能做其他类所能做的任何事，但通常应当保持简单，它往往只提供一些属性，
允许相应的异常处理程序提取有关错误的信息。

大多数异常命名都以 “Error” 结尾，类似标准异常的命名。
'''

## 定义清理操作

'''
try 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作。例如：
'''
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

'''
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt'''

'''
如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。不论 try 语句是否触发异常，
都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：

如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。
如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。

except 或 else 子句执行期间也会触发异常。 同样，该异常会在 finally 子句执行之后被重新触发。

如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。

如果执行 try 语句时遇到 break,continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。

如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，
而不是来自 try 子句的 return 语句的返回值。
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
'result is 2.0'
'executing finally clause'
divide(2, 0)
'division by zero!'
'executing finally clause'
divide("2", "1")
'executing finally clause'
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'''

## 预定义的清理操作

'''
某些对象定义了不需要该对象时要执行的标准清理操作。无论使用该对象的操作是否成功，都会执行清理操作。
比如，下例要打开一个文件，并输出文件内容：
'''
for line in open("myfile.txt"):
    print(line, end="")
'''
这个代码的问题在于，执行完代码后，文件在一段不确定的时间内处于打开状态。在简单脚本中这没有问题，
但对于较大的应用程序来说可能会出问题。with 语句支持以及时、正确的清理的方式使用文件对象：
'''
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


## 引发和处理多个不相关的异常

'''
在有些情况下，有必要报告几个已经发生的异常。这通常是在并发框架中当几个任务并行失败时的情况，但也有其他的用例，
有时需要是继续执行并收集多个错误而不是引发第一个异常。

内置的 ExceptionGroup 打包了一个异常实例的列表，这样它们就可以一起被引发。它本身就是一个异常，
所以它可以像其他异常一样被捕获。
'''
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
'''
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
'''
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')

"caught <class 'ExceptionGroup'>: e"


'''
通过使用 except* 代替 except ，我们可以有选择地只处理组中符合某种类型的异常。
在下面的例子中，显示了一个嵌套的异常组，每个 except* 子句都从组中提取了某种类型的异常，
而让所有其他的异常传播到其他子句，并最终被重新引发。
'''
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
'''
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
'''


'''
注意，嵌套在一个异常组中的异常必须是实例，而不是类型。这是因为在实践中，这些异常通常是那些已经被程序提出并捕获的异常，
其模式如下:
'''
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)

## 用注释细化异常情况


'''
当一个异常被创建以引发时，它通常被初始化为描述所发生错误的信息。在有些情况下，在异常被捕获后添加信息是很有用的。
为了这个目的，异常有一个 add_note(note) 方法接受一个字符串，
并将其添加到异常的注释列表。标准的回溯在异常之后按照它们被添加的顺序呈现包括所有的注释。
'''

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
'''