# 类

'''
类提供了把数据和功能绑定在一起的方法。创建新类时创建了新的对象 类型，从而能够创建该类型的新 实例。
实例具有能维持自身状态的属性，还具有能修改自身状态的方法（由其所属的类来定义）。'''

## 名称和对象

'''
对象之间相互独立，多个名称（甚至是多个作用域内的多个名称）可以绑定到同一对象。这在其他语言中通常被称为别名。
这样做，通常是为了让程序受益，因为别名在某些方面就像指针。例如，传递对象的代价很小，因为实现只传递一个指针；
'''

## Python作用域和命名空间

'''
在介绍类前，首先要介绍 Python 的作用域规则。类定义对命名空间有一些巧妙的技巧，
了解作用域和命名空间的工作机制有利于加强对类的理解。

namespace （命名空间）是从名称到对象的映射。现在，大多数命名空间都使用 Python 字典实现，
但除非涉及到性能优化，我们一般不会关注这方面的事情，而且将来也可能会改变这种方式。

点号之后的名称是 属性。例如，表达式 z.real 中，real 是对象 z 的属性。严格来说，
对模块中名称的引用是属性引用：表达式 modname.funcname 中，modname 是模块对象，funcname 是模块的属性。
模块属性和模块中定义的全局名称之间存在直接的映射：它们共享相同的命名空间！


属性可以是只读的或者可写的。 在后一种情况下，可以对属性进行赋值。 
模块属性是可写的：你可以写入 modname.the_answer = 42 。 
也可以使用 del 语句删除可写属性。 例如，del modname.the_answer 将从名为 modname 对象中移除属性 the_answer。

命名空间是在不同时刻创建的，且拥有不同的生命周期。内置名称的命名空间是在 Python 解释器启动时创建的，永远不会被删除。
模块的全局命名空间在读取模块定义时创建；通常，模块的命名空间也会持续到解释器退出。

函数的局部命名空间在函数被调用时被创建，并在函数返回或抛出未在函数内被处理的异常时，被删除。
（实际上，用“遗忘”来描述实际发生的情况会更好一些。）当然，每次递归调用都有自己的局部命名空间。


作用域虽然是被静态确定的，但会被动态使用。执行期间的任何时刻，都会有 3 或 4 个“命名空间可直接访问”的嵌套作用域：
最内层作用域，包含局部名称，并首先在其中进行搜索
那些外层闭包函数的作用域，包含“非局部、非全局”的名称，从最靠内层的那个作用域开始，逐层向外搜索。
倒数第二层作用域，包含当前模块的全局名称
最外层（最后搜索）的作用域，是内置名称的命名空间


Python 有一个特殊规定。如果不存在生效的 global 或 nonlocal 语句，则对名称的赋值总是会进入最内层作用域。
赋值不会复制数据，只是将名称绑定到对象。删除也是如此：语句 del x 从局部作用域引用的命名空间中移除对 x 的绑定。
所有引入新名称的操作都是使用局部作用域：尤其是 import 语句和函数定义会在局部作用域中绑定模块或函数名称。

global 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定；
nonlocal 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定。
下例演示了如何引用不同作用域和名称空间，以及 global 和 nonlocal 对变量绑定的影响：
'''


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

'''
示例代码的输出是：
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

注意，局部 赋值（这是默认状态）不会改变 scope_test 对 spam 的绑定。 
nonlocal 赋值会改变 scope_test 对 spam 的绑定，而 global 赋值会改变模块层级的绑定。
而且，global 赋值前没有 spam 的绑定。
'''

## 初探类

### 类定义语法
'''
最简单的类定义形式如下：
class ClassName:
    <语句-1>
    .
    .
    .
    <语句-N>

当 (从结尾处) 正常离开类定义时，将创建一个 类对象。 这基本上是一个围绕类定义所创建的命名空间的包装器；
'''

### class对象

'''
类对象支持两种操作：属性引用和实例化。

属性引用 使用 Python 中所有属性引用所使用的标准语法: obj.name。 
有效的属性名称是类对象被创建时存在于类命名空间中的所有名称。 因此，如果类定义是这样的:
'''


class MyClass:
    """一个简单的示例类"""

    i = 12345

    def f(self):
        return 'hello world'


'''
那么 MyClass.i 和 MyClass.f 就是有效的属性引用，将分别返回一个整数和一个函数对象。 
类属性也可以被赋值，因此可以通过赋值来改变 MyClass.i 的值。 __doc__ 也是一个有效的属性，
将返回所属类的文档字符串: "A simple example class"。

类的 实例化 使用函数表示法。 可以把类对象视为是返回该类的一个新实例的不带参数的函数。 举例来说（假设使用上述的类）:
创建类的新 实例 并将此对象分配给局部变量 x。
'''
x = MyClass()
'''
实例化操作 (“调用”类对象) 会创建一个空对象。 许多类都希望创建的对象实例是根据特定初始状态定制的。 
因此一个类可能会定义名为 __init__() 的特殊方法，就像这样:
'''


def __init__(self):
    self.data = []


'''
当一个类定义了 __init__() 方法时，类的实例化会自动为新创建的类实例唤起 __init__()。 
当然，__init__() 方法还有一些参数用于实现更高的灵活性。 在这种情况下，提供给类实例化运算符的参数将被传递给 __init__()。 
例如，
'''


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
x.r, x.i
(3.0, -4.5)

### 实例对象

'''
实例对象所能理解的唯一操作是属性引用。 有两种有效的属性名称：数据属性和方法。
'''

### 方法对象

'''
通常，方法在绑定后立即被调用:
x.f()
但是，方法并不是必须立即调用: x.f 是一个方法对象，它可以被保存起来以后再调用。
xf = x.f
while True:
    print(xf())
'''


'''
当一个方法被调用时究竟会发生什么？ 你可能已经注意到尽管 f() 的函数定义指定了一个参数，但上面调用 x.f() 时却没有带参数。 
这个参数发生了什么事？ 当一个需要参数的函数在不附带任何参数的情况下被调用时 Python 肯定会引发异常 --- 
即使参数实际上没有被使用...

实际上，你可能已经猜到了答案：方法的特殊之处就在于实例对象会作为函数的第一个参数被传入。 
在我们的示例中，调用 x.f() 其实就相当于 MyClass.f(x)。 
总之，调用一个具有 n 个参数的方法就相当于调用再多一个参数的对应函数，这个参数值为方法所属实例对象，
位置在其他参数之前。
'''


### 类和实例变量

'''
一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法:
'''


class Dog:

    kind = 'canine'  # 类变量被所有实例所共享

    def __init__(self, name):
        self.name = name  # 实例变量为每个实例所独有


d = Dog('Fido')
e = Dog('Buddy')
d.kind  # 被所有的 Dog 实例所共享
'canine'
e.kind  # 被所有的 Dog 实例所共享
'canine'
d.name  # 为 d 所独有
'Fido'
e.name  # 为 e 所独有
'Buddy'


'''
正如 名称和对象 中已讨论过的，共享数据可能在涉及 mutable 对象例如列表和字典的时候导致令人惊讶的结果。 
例如以下代码中的 tricks 列表不应该被用作类变量，因为所有的 Dog 实例将只共享一个单独的列表:
'''


class Dog:

    tricks = []  # 类变量的错误用法

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks  # 非预期地被所有的 Dog 实例所共享
['roll over', 'play dead']

'正确的类设计应该使用实例变量:'


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # 为每个 Dog 实例新建一个空列表

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
['roll over']
e.tricks
['play dead']


## 补充说明

'''
如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:
'''


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
'storage west'
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
'storage east'

'''
数据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。 换句话说，类不能用于实现纯抽象数据类型。 
实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。 
（而在另一方面，用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；
此特性可以通过用 C 编写 Python 扩展来使用。）
'''

## 继承

'''
当然，如果不支持继承，语言特性就不值得称为“类”。派生类定义的语法如下所示:
class DerivedClassName(BaseClassName):
    <语句-1>
    .
    .
    .
    <语句-N>

名称 BaseClassName 必须定义于可从包含所派生的类的定义的作用域访问的命名空间中。 
作为基类名称的替代，也允许使用其他任意表达式。 例如，当基类定义在另一个模块中时，这就会很有用处:

class DerivedClassName(modname.BaseClassName):
派生类定义的执行过程与基类相同。 当构造类对象时，基类会被记住。 
此信息将被用来解析属性引用：如果请求的属性在类中找不到，搜索将转往基类中进行查找。 
如果基类本身也派生自其他某个类，则此规则将被递归地应用。

派生类的实例化没有任何特殊之处: DerivedClassName() 会创建该类的一个新实例。 
方法引用将按以下方式解析：搜索相应的类属性，如有必要将按基类继承链逐步向下查找，如果产生了一个函数对象则方法引用就生效。

派生类可能会重写其基类的方法。 因为方法在调用同一对象的其他方法时没有特殊权限，
所以基类方法在尝试调用调用同一基类中定义的另一方法时，可能实际上调用是该基类的派生类中定义的方法。
（对 C++ 程序员的提示：Python 中所有的方法实际上都是 virtual 方法。）

Python有两个内置函数可被用于继承机制：

使用 isinstance() 来检查一个实例的类型: isinstance(obj, int) 仅会在 obj.__class__ 为 int 或某个派生自 int 的类时为 True。

使用 issubclass() 来检查类的继承关系: issubclass(bool, int) 为 True，因为 bool 是 int 的子类。 
但是，issubclass(float, int) 为 False，因为 float 不是 int 的子类。

'''

### 多重继承

'''
Python 也支持一种多重继承。 带有多个基类的类定义语句如下所示:
class DerivedClassName(Base1, Base2, Base3):
    <语句-1>
    .
    .
    .
    <语句-N>
对于多数目的来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左到右的，
当层次结构存在重叠时不会在同一个类中搜索两次。 因此，如果某个属性在 DerivedClassName 中找不到，就会在 Base1 中搜索它，
然后（递归地）在 Base1 的基类中搜索，如果在那里也找不到，就将在 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用。 
这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

动态调整顺序是有必要的，因为所有多重继承的情况都会显示出一个或更多的菱形关联
（即至少有一个上级类可通过多条路径被最底层的类所访问）。 例如，所有类都是继承自 object，
因此任何多重继承的情况都提供了一条以上的路径可以通向 object。 为了确保基类不会被访问一次以上，
动态算法会用一种特殊方式将搜索顺序线性化，保留每个类所指定的从左至右的顺序，只调用每个上级类一次，
并且保持单调性（即一个类可以被子类化而不影响其父类的优先顺序）。 
总而言之，这些特性使得设计具有多重继承的可靠且可扩展的类成为可能。
'''

## 私有变量

'''
那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：
带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 名称改写。 
任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 _classname__spam，
其中 classname 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重写方法而不破坏类内方法调用。例如:
'''


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # 原始 update() 方法的私有副本


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # 为 update() 提供了新的签名
        # 但不会破坏 __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


'''
上面的示例即使在 MappingSubclass 引入了一个 __update 标识符的情况下也不会出错，
因为它会在 Mapping 类中被替换为 _Mapping__update 而在 MappingSubclass 类中被替换为 _MappingSubclass__update。

请注意，改写规则的设计主要是为了避免意外冲突；访问或修改被视为私有的变量仍然是可能的。
'''

## 杂项说明

'''
有时具有类似于 Pascal "record" 或 C "struct" 的数据类型是很有用的，将一些带名称的数据项捆绑在一起。 
实现这一目标的理想方式是使用 dataclasses:
'''
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


john = Employee('john', 'computer lab', 1000)
john.dept
'computer lab'
john.salary
1000

## 迭代器

'''
到目前为止，您可能已经注意到大多数容器对象都可以使用 for 语句:
'''
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

'''
这种访问风格清晰、简洁又方便。 迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 
在幕后，for 语句会在容器对象上调用 iter()。 该函数返回一个定义了 __next__() 方法的迭代器对象，
此方法将逐一访问容器中的元素。 当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 
你可以使用 next() 内置函数来调用 __next__() 方法；这个例子显示了它的运作方式:
'''
s = 'abc'
it = iter(s)
it
'<str_iterator object at 0x10c90e650>'
next(it)
'a'
next(it)
'b'
next(it)
'c'
next(it)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
'''

'''
了解了迭代器协议背后的机制后，就可以轻松地为你的类添加迭代器行为了。 
定义 __iter__() 方法用于返回一个带有 __next__() 方法的对象。 
如果类已定义了 __next__()，那么 __iter__() 可以简单地返回 self:
'''


class Reverse:
    """对一个序列执行反向循环的迭代器。"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
'<__main__.Reverse object at 0x00A1DB50>'
for char in rev:
    print(char)
'''
m
a
p
s
'''

## 生成器

'''
生成器 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似于标准的函数，但当它们要返回数据时会使用 yield 语句。 
每次在生成器上调用 next() 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）。 
一个显示如何非常容易地创建生成器的示例如下:
'''


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)
'''
f
l
o
g
'''

# 可以用生成器来完成的任何功能同样可以通用前一节所描述的基于类的迭代器来完成。
# 但生成器的写法更为紧凑，因为它会自动创建 __iter__() 和 __next__() 方法。

# 另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。
# 这使得该函数相比使用 self.index 和 self.data 这种实例变量的方式更易编写且更为清晰。

# 除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 StopIteration。
# 这些特性结合在一起，使得创建迭代器能与编写常规函数一样容易。

## 生成器表达式

'''
某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。 
这种表达式被设计用于生成器将立即被外层函数所使用的情况。 生成器表达式相比完整的生成器更紧凑但较不灵活，
相比等效的列表推导式则更为节省内存。
'''
sum(i * i for i in range(10))  # 平方和
285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x * y for x, y in zip(xvec, yvec))  # 点乘
260

unique_words = set(word for line in page for word in line.split())  # type:ignore

valedictorian = max((student.gpa, student.name) for student in graduates)  # type:ignore

data = 'golf'
list(data[i] for i in range(len(data) - 1, -1, -1))
['f', 'l', 'o', 'g']
