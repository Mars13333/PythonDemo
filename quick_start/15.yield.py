# 在 Python 中，yield 是一个关键字，用于定义生成器函数（generator function）。
# 生成器是一种特殊的迭代器，它可以在迭代过程中“暂停”和“恢复”执行，
# 从而实现按需生成数据，而不是一次性生成所有数据。
# 这使得生成器在处理大量数据或实现惰性求值时非常高效。


# 1 定义生成器函数
# 使用 yield 的函数被称为生成器函数。
# 当调用生成器函数时，它不会像普通函数那样直接执行代码，而是返回一个生成器对象。
# 生成器对象可以通过迭代器协议（__iter__ 和 __next__）逐个生成值。

# 2 生成数据
# 在生成器函数中，yield 用于生成一个值，并暂停函数的执行。
# 当生成器的 __next__ 方法被调用时，函数会从上次暂停的地方继续执行，
# 直到遇到下一个 yield 语句。

# 3 惰性求值
# 生成器是惰性求值的，即只有在需要时才会生成下一个值。
# 这使得生成器在处理大量数据时非常高效，因为它不会一次性占用大量内存。


# 示例 简单生成器
def simple_generator():
    yield 1
    yield 2
    yield 3

# 创建生成器对象
gen = simple_generator()

# 逐个生成值
print(next(gen))  # 输出: 1
# print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3/2

print("-----------------------")


# 示例2 生成器用于生成序列
def generate_numbers(n):
  for i in range(n):
    yield i

# 创建生成器对象
num_gen = generate_numbers(5)
# 逐个生成值
for num in num_gen:
  print(num)

print("-----------------------")


# yield 高级用法

# 示例1 生成器表达式
# 生成器表达式类似于列表推导式，但使用圆括号 () 而不是方括号 []，
# 并且生成器表达式是惰性求值的。

gen =(x*x for x in range(5))
# 逐个获取生成值
for num in gen:
  print(num)


print("-----------------------")


# 示例2 在异步函数中使用yield ！！！
# 在异步函数中，yield 可以用于生成异步生成器。异步生成器可以与 async for 一起使用，
# 逐个生成异步数据。

import asyncio

async def async_gen():
  for i in range(3):
    await asyncio.sleep(1) # 模拟耗时操作
    yield i

# 使用async for 迭代异步生成器
async def main():
  async for num in async_gen():
    print(num)

asyncio.run(main())


print("-----------------------")


# yield的作用

# 1 生成数据
# yield 用于生成一个值，并暂停函数的执行。
# 每次调用生成器的 __next__ 方法时，函数会从上次暂停的地方继续执行，直到遇到下一个 yield 语句。


# 2 惰性求值
# 生成器是惰性求值的，即只有在需要时才会生成下一个值。
# 这使得生成器在处理大量数据时非常高效，因为它不会一次性占用大量内存。


# 3 实现迭代器协议
# 生成器函数返回一个生成器对象，生成器对象实现了迭代器协议（__iter__ 和 __next__）。
# 可以通过 for 循环或 next() 函数逐个获取生成器的值。
