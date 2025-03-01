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

## 触发异常


## 异常链


## 用户自定义异常


## 定义清理操作


## 预定义的清理操作

## 引发和处理多个不相关的异常

## 用注释细化异常情况
