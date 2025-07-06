import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    

# ============================================================================
# 代码分析说明
# ============================================================================

# 1. ranks 的作用：
# ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# - [str(n) for n in range(2, 11)] 生成 ['2', '3', '4', '5', '6', '7', '8', '9', '10']
# - list('JQKA') 生成 ['J', 'Q', 'K', 'A']
# - 最终 ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# - 总共13种点数

# 2. suits 的作用：
# suits = 'spades diamonds clubs hearts'.split()
# - 'spades diamonds clubs hearts' 是一个字符串
# - .split() 方法按空格分割字符串
# - 最终 suits = ['spades', 'diamonds', 'clubs', 'hearts']
# - 总共4种花色

# 3. 为什么 len(deck) 返回 52？
# 在 __init__ 方法中：
# self._cards = [Card(rank, suit) for suit in self.suits
#                                 for rank in self.ranks]
# 
# 这是一个嵌套列表推导式，等价于：
# 多个 for 子句时，从左到右，从外到内，依次执行！！！
# self._cards = []
# for suit in self.suits:      # 4种花色
#     for rank in self.ranks:  # 13种点数
#         self._cards.append(Card(rank, suit))
# 
# 计算过程：
# - 花色数量：4（spades, diamonds, clubs, hearts）
# - 点数数量：13（2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A）
# - 总牌数：4 × 13 = 52

# 4. 为什么 deck[0] 返回 Card('2', 'spades')？
# 生成顺序（简化版）：
# suit='spades', rank='2' → Card('2', 'spades')     # 第1张 (deck[0])
# suit='spades', rank='3' → Card('3', 'spades')     # 第2张 (deck[1])
# suit='spades', rank='4' → Card('4', 'spades')     # 第3张 (deck[2])
# ...
# suit='spades', rank='A' → Card('A', 'spades')     # 第13张 (deck[12])
# suit='diamonds', rank='2' → Card('2', 'diamonds') # 第14张 (deck[13])
# ...
# suit='hearts', rank='A' → Card('A', 'hearts')     # 第52张 (deck[51])

# 5. split() 方法说明：
# split() 默认按空格分割字符串
# 'hello world'.split()  # ['hello', 'world']
# 'apple,banana,orange'.split(',')  # ['apple', 'banana', 'orange']

# 6. 嵌套循环的生成顺序：
# 外层循环：花色
# for suit in ['spades', 'diamonds', 'clubs', 'hearts']:
#     内层循环：点数
#     for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
#         生成每张牌

# 7. 为什么是 52 张牌？
# - 标准扑克牌就是 52 张
# - 4 种花色 × 13 种点数 = 52 张
# - 这样设计完美模拟了真实的扑克牌组

# ============================================================================
# 使用示例：
# ============================================================================
# >>> from L01_FrenchDeck import Card, FrenchDeck
# >>> deck = FrenchDeck()
# >>> len(deck)  # 52
# >>> deck[0]    # Card(rank='2', suit='spades')
# >>> deck[-1]   # Card(rank='A', suit='hearts')
# >>> deck[12]   # Card(rank='A', suit='spades')
# >>> deck[13]   # Card(rank='2', suit='diamonds')

# ============================================================================
# Python 特殊函数（魔术方法）详解
# ============================================================================

# 1. __len__(self) - 长度函数
# 作用：定义 len() 函数的行为
# 示例：len(deck) 会调用 deck.__len__()
# def __len__(self):
#     return len(self._cards)

# 2. __getitem__(self, position) - 索引访问
# 作用：定义 obj[index] 的行为
# 示例：deck[0] 会调用 deck.__getitem__(0)
# def __getitem__(self, position):
#     return self._cards[position]

# 3. __setitem__(self, key, value) - 索引赋值
# 作用：定义 obj[index] = value 的行为
# 示例：
# def __setitem__(self, key, value):
#     self._cards[key] = value

# 4. __delitem__(self, key) - 删除索引
# 作用：定义 del obj[index] 的行为
# 示例：
# def __delitem__(self, key):
#     del self._cards[key]

# 5. __contains__(self, item) - 成员检查
# 作用：定义 item in obj 的行为
# 示例：
# def __contains__(self, item):
#     return item in self._cards

# 6. __iter__(self) - 迭代器
# 作用：定义 for item in obj 的行为
# 示例：
# def __iter__(self):
#     return iter(self._cards)

# 7. __next__(self) - 下一个元素
# 作用：定义迭代器的下一个元素
# 示例：
# def __next__(self):
#     if self._index >= len(self._cards):
#         raise StopIteration
#     result = self._cards[self._index]
#     self._index += 1
#     return result

# 8. __str__(self) - 字符串表示
# 作用：定义 str(obj) 的行为
# 示例：
# def __str__(self):
#     return f"FrenchDeck with {len(self._cards)} cards"

# 9. __repr__(self) - 详细字符串表示
# 作用：定义 repr(obj) 的行为，用于调试
# 示例：
# def __repr__(self):
#     return f"FrenchDeck(cards={self._cards})"

# 10. __eq__(self, other) - 相等比较
# 作用：定义 obj == other 的行为
# 示例：
# def __eq__(self, other):
#     if not isinstance(other, FrenchDeck):
#         return False
#     return self._cards == other._cards

# 11. __lt__(self, other) - 小于比较
# 作用：定义 obj < other 的行为
# 示例：
# def __lt__(self, other):
#     return len(self._cards) < len(other._cards)

# 12. __hash__(self) - 哈希值
# 作用：定义 hash(obj) 的行为
# 示例：
# def __hash__(self):
#     return hash(tuple(self._cards))

# 13. __call__(self, *args, **kwargs) - 可调用对象
# 作用：定义 obj() 的行为，让对象可以像函数一样调用
# 示例：
# def __call__(self, index):
#     return self._cards[index]

# 14. __enter__(self) 和 __exit__(self, exc_type, exc_val, exc_tb) - 上下文管理器
# 作用：定义 with obj: 的行为
# 示例：
# def __enter__(self):
#     return self
# 
# def __exit__(self, exc_type, exc_val, exc_tb):
#     pass

# 15. __add__(self, other) - 加法
# 作用：定义 obj + other 的行为
# 示例：
# def __add__(self, other):
#     if isinstance(other, FrenchDeck):
#         return FrenchDeck(self._cards + other._cards)

# 16. __sub__(self, other) - 减法
# 作用：定义 obj - other 的行为

# 17. __mul__(self, other) - 乘法
# 作用：定义 obj * other 的行为

# 18. __truediv__(self, other) - 除法
# 作用：定义 obj / other 的行为

# 19. __floordiv__(self, other) - 整除
# 作用：定义 obj // other 的行为

# 20. __mod__(self, other) - 取模
# 作用：定义 obj % other 的行为

# ============================================================================
# 特殊函数分类总结：
# ============================================================================

# 1. 基本操作：
# - __len__() - 长度
# - __bool__() - 布尔值
# - __str__() - 字符串表示
# - __repr__() - 详细表示

# 2. 属性访问：
# - __getattr__(self, name) - 获取属性
# - __setattr__(self, name, value) - 设置属性
# - __delattr__(self, name) - 删除属性
# - __getattribute__(self, name) - 获取属性（优先级更高）

# 3. 容器操作：
# - __getitem__() - 索引访问
# - __setitem__() - 索引赋值
# - __delitem__() - 删除索引
# - __contains__() - 成员检查
# - __iter__() - 迭代器
# - __next__() - 下一个元素

# 4. 比较操作：
# - __eq__() - 等于
# - __ne__() - 不等于
# - __lt__() - 小于
# - __le__() - 小于等于
# - __gt__() - 大于
# - __ge__() - 大于等于

# 5. 算术操作：
# - __add__() - 加法
# - __sub__() - 减法
# - __mul__() - 乘法
# - __truediv__() - 除法
# - __floordiv__() - 整除
# - __mod__() - 取模
# - __pow__() - 幂运算

# 6. 其他：
# - __call__() - 可调用对象
# - __enter__() / __exit__() - 上下文管理器
# - __hash__() - 哈希值

# ============================================================================
# 实际应用示例：
# ============================================================================

# 在 FrenchDeck 中添加更多特殊函数：

# class FrenchDeck:
#     # ... 现有代码 ...
#     
#     def __str__(self):
#         return f"FrenchDeck with {len(self._cards)} cards"
#     
#     def __contains__(self, card):
#         return card in self._cards
#     
#     def __iter__(self):
#         return iter(self._cards)
#     
#     def __eq__(self, other):
#         if not isinstance(other, FrenchDeck):
#             return False
#         return self._cards == other._cards

# 使用示例：
# >>> deck = FrenchDeck()
# >>> str(deck)  # "FrenchDeck with 52 cards"
# >>> Card('7', 'diamonds') in deck  # True
# >>> for card in deck[:3]:  # 可以迭代
# ...     print(card)
# >>> deck2 = FrenchDeck()
# >>> deck == deck2  # True
    
    