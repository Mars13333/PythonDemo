# 定义函数
# 定义 函数使用关键字 def，后跟函数名与括号内的形参列表。函数语句从下一行开始，并且必须缩进。
# 函数内的第一条语句是字符串时，该字符串就是文档字符串，也称为 docstring，详见 文档字符串。
# 利用文档字符串可以自动生成在线文档或打印版文档，还可以让开发者在浏览代码时直接查阅文档；
# Python 开发者最好养成在代码中加入文档字符串的好习惯。
# 下列代码创建一个可以输出限定数值内的斐波那契数列函数：
def fib(n):  # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# 现在调用我们刚定义的函数：
fib(2000)
'0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597'


# 函数定义在当前符号表中把函数名与函数对象关联在一起。解释器把函数名指向的对象作为用户自定义函数。
# 还可以使用其他名称指向同一个函数对象，并访问访该函数：
fib
'<function fib at 10042ed0>'
f = fib
f(100)
'0 1 1 2 3 5 8 13 21 34 55 89'
# 如果你用过其他语言，你可能会认为 fib 不是函数而是一个过程，因为它没有返回值。
# 事实上，即使没有 return 语句的函数也有返回值，尽管这个值可能相当无聊。 这个值被称为 None (是一个内置名称)。
# 通常解释器会屏蔽单独的返回值 None。 如果你确有需要可以使用 print() 查看它:
# fib(0)
print(fib(0))
None


# ------------------------------------------------------------------------


# 默认参数值
# 为参数指定默认值是非常有用的方式。调用函数时，可以使用比定义时更少的参数，例如：
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 该函数可以用以下方式调用：
# 只给出必选实参：ask_ok('Do you really want to quit?')
# 给出一个可选实参：ask_ok('OK to overwrite the file?', 2)
# 给出所有实参：ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# 本例还使用了关键字 in ，用于确认序列中是否包含某个值。


# 重要警告： 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。
# 例如，下面的函数会累积后续调用时传递的参数：
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
# 输出结果如下：
[1]
[1, 2]
[1, 2, 3]


# 不想在后续调用之间共享默认值时，应以如下方式编写函数：
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# ------------------------------------------------------------------------


# 关键字参数 kwarg=value 形式的 关键字参数 也可以用于调用函数。函数示例如下：
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 该函数接受一个必选参数（voltage）和三个可选参数（state, action 和 type）。该函数可用下列方式调用：
parrot(1000)  # 1 个位置参数
parrot(voltage=1000)  # 1 个关键字参数
parrot(voltage=1000000, action='VOOOOOM')  # 2 个关键字参数
parrot(action='VOOOOOM', voltage=1000000)  # 2 个关键字参数
parrot('a million', 'bereft of life', 'jump')  # 3 个位置参数
parrot('a thousand', state='pushing up the daisies')  # 1 个位置参数，1 个关键字参数

# 以下调用函数的方式都无效：
parrot()  # 缺失必需的参数
# parrot(voltage=5.0, 'dead')  # 关键字参数后存在非关键字参数
parrot(110, voltage=220)  # 同一个参数重复的值
parrot(actor='John Cleese')  # 未知的关键字参数


# 最后一个形参为 **name 形式时，接收一个字典（详见 映射类型 --- dict），该字典包含与函数中已定义形参对应之外的所有关键字参数。
# **name 形参可以与 *name 形参（下一小节介绍）组合使用（*name 必须在 **name 前面），
# *name 形参接收一个 元组，该元组包含形参列表之外的位置参数。例如，可以定义下面这样的函数：
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# 该函数可以用如下方式调用：
cheeseshop(
    "Limburger",
    "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
)
# 输出结果如下：
'''
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
'''


# ------------------------------------------------------------------------


# 特殊参数
# 默认情况下，参数可以按位置或显式关键字传递给 Python 函数。为了让代码易读、高效，最好限制参数的传递方式，
# 这样，开发者只需查看函数定义，即可确定参数项是仅按位置、按位置或关键字，还是仅按关键字传递。
# 函数定义如下：
'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        位置或关键字   |
        |                                - 仅限关键字
         -- 仅限位置
'''


# / 和 * 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。关键字形参也叫作命名形参。
# 此处再介绍一些细节，特定形参可以标记为 仅限位置。仅限位置 时，形参的顺序很重要，且这些形参不能用关键字传递。
# 仅限位置形参应放在 / （正斜杠）前。/ 用于在逻辑上分割仅限位置形参与其它形参。
# 如果函数定义中没有 /，则表示没有仅限位置形参。
# / 后可以是 位置或关键字 或 仅限关键字 形参。
# 把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字 形参前添加 *。


# 请看下面的函数定义示例，注意 / 和 * 标记：
def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):  # 仅位置
    print(arg)


def kwd_only_arg(*, arg):  # 仅关键字
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# 第一个函数定义 standard_arg 是最常见的形式，对调用方式没有任何限制，可以按位置也可以按关键字传递参数：
standard_arg(2)
2

standard_arg(arg=2)
2

# 第二个函数 pos_only_arg 的函数定义中有 /，仅限使用位置形参：
pos_only_arg(1)
1

pos_only_arg(arg=1)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
'''


# 第三个函数 kwd_only_arg 如在函数定义中通过 * 所指明的那样只允许关键字参数。
kwd_only_arg(3)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
'''
kwd_only_arg(arg=3)
3


# 最后一个函数在同一个函数定义中，使用了全部三种调用惯例：
combined_example(1, 2, 3)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
'''
combined_example(1, 2, kwd_only=3)
'1 2 3'

combined_example(1, standard=2, kwd_only=3)
'1 2 3'

combined_example(pos_only=1, standard=2, kwd_only=3)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
'''


# 下面的函数定义中，kwds 把 name 当作键，因此，可能与位置参数 name 产生潜在冲突：
def foo(name, **kwds):
    return 'name' in kwds


# 调用该函数不可能返回 True，因为关键字 'name' 总与第一个形参绑定。例如：
foo(1, **{'name': 2})
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
'''


# 加上 / （仅限位置参数）后，就可以了。此时，函数定义把 name 当作位置参数，'name' 也可以作为关键字参数的键：
def foo(name, /, **kwds):
    return 'name' in kwds


foo(1, **{'name': 2})
True
# 换句话说，仅限位置形参的名称可以在 **kwds 中使用，而不产生歧义。


# ------------------------------------------------------------------------


#  解包实参列表
# 函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。
# 例如，内置的 range() 函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，
# 用 * 操作符把实参从列表或元组解包出来
list(range(3, 6))  # 附带两个参数的正常调用
[3, 4, 5]
args = [3, 6]
list(range(*args))  # 附带从一个 列表解包 的参数的调用
[3, 4, 5]


# 同样，字典可以用 ** 操作符传递关键字参数：
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
"-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !"


# ------------------------------------------------------------------------


# lambda表达式
# lambda 关键字用于创建小巧的匿名函数。lambda a, b: a+b 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。
# 在语法上，匿名函数只能是单个表达式。在语义上，它只是常规函数定义的语法糖。
# 与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量：
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(0)
42
f(1)
43

# 上例用 lambda 表达式返回函数。还可以把匿名函数用作传递的实参：
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# ------------------------------------------------------------------------

# 文档字符串
# 第一行应为对象用途的简短摘要。为保持简洁，不要在这里显式说明对象名或类型，
# 因为可通过其他方式获取这些信息（除非该名称碰巧是描述函数操作的动词）。这一行应以大写字母开头，以句点结尾。
# 文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开。后面的行可包含若干段落，描述对象的调用约定、副作用等。


# 下面是多行文档字符串的一个例子：
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
'''
Do nothing, but document it.

    No, really, it doesn't do anything.
'''


# ------------------------------------------------------------------------


# 函数注解
# 函数注解 是可选的用户自定义函数类型的元数据完整信息
# 标注 以字典的形式存放在函数的 __annotations__ 属性中而对函数的其他部分没有影响。
# 形参标注的定义方式是在形参名后加冒号，后面跟一个会被求值为标注的值的表达式。
# 返回值标注的定义方式是加组合符号 ->，后面跟一个表达式，这样的校注位于形参列表和表示 def 语句结束的冒号。
# 下面的示例有一个必须的参数、一个可选的关键字参数以及返回值都带有相应的标注:
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
'''
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
'''
