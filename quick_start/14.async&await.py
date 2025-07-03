# 同步代码
import time

def task1():
  print('task1 start')
  time.sleep(2)
  print('task1 end')

def task2():
  print('task2 start')
  time.sleep(2)
  print('task2 end')

# 同步执行
def sync():
  task1()
  task2()

# sync() # 同步执行，耗时4秒
# Task 1 started
# （等待2秒）
# Task 1 completed
# Task 2 started
# （等待2秒）
# Task 2 completed


#######################################

import asyncio

async def task3():
  print('task3 start')
  await asyncio.sleep(2)
  print('task3 end')

async def task4():
  print('task4 start')
  await asyncio.sleep(2)
  print('task4 end')

async def async_run(): # 异步执行
  await asyncio.gather(task3(), task4())

asyncio.run(async_run())
# task3 start
# task4 start
# （等待2秒）
# task3 end
# task4 end