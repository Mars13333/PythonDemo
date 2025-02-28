# if
# 可有零个或多个 elif 部分，else 部分也是可选的。关键字 'elif' 是 'else if' 的缩写，用于避免过多的缩进。
# if ... elif ... elif ... 序列可以当作其它语言中 switch 或 case 语句的替代品。

x = 33
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# ------------------------------------------------------------------------


# for
# Python 的 for 语句与 C 或 Pascal 中的不同。
# Python 的 for 语句不迭代算术递增数值（如 Pascal），
# 或是给予用户定义迭代步骤和结束条件的能力（如 C），而是在列表或字符串等任意序列的元素上迭代，按它们在序列中出现的顺序。
# 度量一些字符串：
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

'''
cat 3
window 6
defenestrate 12
'''

# 很难正确地在迭代多项集的同时修改多项集的内容。更简单的方法是迭代多项集的副本或者创建新的多项集：
# 创建示例多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 策略：迭代一个副本
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 策略：创建一个新多项集
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# ------------------------------------------------------------------------


# range 内置函数 range() 用于生成等差数列：
for i in range(5):
    print(i)
0
1
2
3
4


# 生成的序列绝不会包括给定的终止值；range(10) 生成 10 个值——长度为 10 的序列的所有合法索引。
# range 可以不从 0 开始，且可以按给定的步长递增（即使是负数步长）：
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]


# 要按索引迭代序列，可以组合使用 range() 和 len()：
# 不过大多数情况下 enumerate() 函数很方便，详见 循环的技巧。
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

'''
0 Mary
1 had
2 a
3 little
4 lamb
'''

# 如果直接打印一个 range 会发生意想不到的事情：
range(10)
'''range(0, 10)'''
# range() 返回的对象在很多方面和列表的行为一样，但其实它和列表不一样。
# 该对象只有在被迭代时才一个一个地返回所期望的列表项，并没有真正生成过一个含有全部项的列表，
# 从而节省了空间。
# 这种对象称为可迭代对象 iterable，适合作为需要获取一系列值的函数或程序构件的参数。
# for 语句就是这样的程序构件；以可迭代对象作为参数的函数例如 sum()：
sum(range(4))  # 0 + 1 + 2 + 3
6
# 之后我们会看到更多返回可迭代对象，或以可迭代对象作为参数的函数。在 数据结构 这一章中，我们将讨论 list() 的更多细节。


# ------------------------------------------------------------------------


# break和continue
# break 语句将跳出最近的一层 for 或 while 循环:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
'''
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
'''

# continue 语句将继续执行循环的下一次迭代:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

'''
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''


# ------------------------------------------------------------------------


# 循环的else语句
# 当配合循环使用时，else 子句更像是 try 语句的 else 子句而不像 if 语句的相应子句：
# 一个 try 语句的 else 子句会在未发生异常时运行，而一个循环的 else 子句会在未发生 break 时运行。

# 在 for 或 while 循环中 break 语句可能对应一个 else 子句。 如果循环在未执行 break 的情况下结束，else 子句将会执行。
# 在 for 循环中，else 子句会在循环结束其他最后一次迭代之后，即未执行 break 的情况下被执行。
# 在 while 循环中，它会在循环条件变为假值后执行。
# 在这两类循环中，当在循环被 break 终结时 else 子句 不会 被执行。 当然，其他提前结束循环的方式，如 return 或是引发异常，也会跳过 else 子句的执行。

# 下面的搜索质数的 for 循环就是一个例子：
# （对，这是正确的代码。 仔细看：其中 else 子句属于 for 循环，而 不属于 if 语句。）
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # 因数
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # 质数
        print(n, 'is a prime number')

'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
'''


# ------------------------------------------------------------------------


# pass
# pass 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句。例如：
while True:
    pass  # 无限等待键盘中断 (Ctrl+C)


# 这常用于创建一个最小的类：
class MyEmptyClass:
    pass


# pass 还可用作函数或条件语句体的占位符，让你保持在更抽象的层次进行思考。pass 会被默默地忽略：
def initlog(*args):
    pass  # 记得实现这个！


# ------------------------------------------------------------------------


# match
# match 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。
# 这表面上像 C、Java 或 JavaScript（以及许多其他程序设计语言）中的 switch 语句，
# 但其实它更像 Rust 或 Haskell 中的模式匹配。只有第一个匹配的模式会被执行，
# 并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。


# 最简单的形式是将一个主语值与一个或多个字面值进行比较：
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# 注意最后一个代码块：“变量名” _ 被作为 通配符 并必定会匹配成功。如果没有 case 匹配成功，则不会执行任何分支。
# 你可以用 | （“或”）将多个字面值组合到一个模式中：
'''
case 401 | 403 | 404:
    return "Not allowed"
'''


# 形如解包赋值的模式可被用于绑定变量：
# point 是一个 (x, y) 元组
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# 请仔细学习此代码！第一个模式有两个字面值，可视为前述字面值模式的扩展。接下来的两个模式结合了一个字面值和一个变量，
# 变量 绑定 了来自主语（point）的一个值。第四个模式捕获了两个值，使其在概念上与解包赋值 (x, y) = point 类似。


# 如果用类组织数据，可以用“类名后接一个参数列表”这种很像构造器的形式，把属性捕获到变量里：
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


# 我们可以为模式添加 if 作为守卫子句。如果守卫子句的值为假，那么 match 会继续尝试匹配下一个 case 块。
# 注意是先将值捕获，再对守卫子句求值：
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


# 模式可以使用具名常量。它们必须作为带点号的名称出现，以防止它们被解释为用于捕获的变量：
from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
