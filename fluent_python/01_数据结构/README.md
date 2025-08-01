第1章介绍Python数据模型，说明为什么`特殊方法`（例如__repr__）是所有类型的对象在行为上保持一致的关键。特殊方法在书中各章有深入的讲解。

接下来的几章介绍各种`容器类型`，包括`序列(sequence)`、`映射(mapping)`和`集合(set)`，另外还涉及`字符串(str)`和`字节序列(bytes)`的区别。
说起来，这是让亲者（Python3用户）快、仇者（Python2用户）痛的一个关键，因其使代码迁移难度陡增。

另外，这一部分还讲到标准库中的**高级类构建器**：`具名元组工厂`和`@dataclass装饰器`。
Python3.10新引入的`模式匹配`在第2章、第3章和第5章的几节中有讨论，涉及序列模式、映射模式和类模式。

第6章关注`对象的生命周期`：`引用`、`可变性`和`垃圾回收`。


tasks:

- 搭建win下python环境，使得可以在命令行终端执行python代码