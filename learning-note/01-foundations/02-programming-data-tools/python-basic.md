1. 编译型 和 解释型

2. 标识符命名规则
    字母、数字、下划线；不能数字开头，不能空格；区分大小写；不能使用Python关键字
    小驼峰userName
    大驼峰UserName
    蛇形user_name

3. 限制传参
    斜杠(/)规则：在函数定义中，斜杠前的参数必须使用位置参数传递。例如在`def greet(name, /, ...)`中，`name`必须通过位置参数传递。
    星号(*)规则：星号后的参数必须使用关键字参数传递。例如在`def greet(..., *, age, height)`中，`age`和height必须通过关键字参数传递。
    混合使用：斜杠和星号可以同时使用，但斜杠必须位于星号之前。例如`def greet(name, /, gender, *, age, height)`是合法的。

4. 可变参数
   - 位置参数：`*args`
   - 关键字参数：`**kwargs`

5. 函数作用域
   LEGB规则：Python查找变量时按顺序检查Local→Enclosing→Global→Built-in作用域
   - 全局作用域Global 在函数内 以global关键字声明
   - 局部作用域Local 
   - 外层作用域Enclosing 当函数内部定义另一个函数时，外层函数的作用域 nonlocal关键字声明
   - 内建作用域Built-in
  
6. 装饰器
   `@property` ：getter方法，使方法像属性一样调用输出结果
   `@setter` ：setter方法，使方法像属性一样修改属性值

7. 多态
   同一个方法，被不同的对象调用，有不同的实现
   - 标准多态：继承关系，重写方法，父类类型限制
   - 鸭子多态：只要不同的对象拥有同名的方法，你就可以用同样的代码去调用它们

8. 抽象类
   `@abstractmethod`作为模板定义公共属性和行为契约，侧重于代码复用和类型约束
   - 不能被实例化
   - 普通方法直接继承
   - 抽象方法必须在子类中实现

9.  数据处理函数
   - `result = map(func, data)`：对一组数据中的每一个元素统一执行某种操作（加工），并生成一组新数据
   - `result = filter(func, data)`：从一组数据中筛选出符合条件的元素（过滤），并组成一组新数据
   - `result = reduce(func, data)`：将一组数据通过"滚雪球"式的操作不断合并，最终归并成一个结果
   - `result = sorted(data)`：对一组数据进行排序，返回一组新数据，不会修改原数据。

10. 闭包
    不用全局变量或类，就能在多次调用间保存数据。修改外层作用域的变量时，需要使用nonlocal关键字声明。
    - 存在嵌套函数（内层函数定义在外层函数内）
    - 内层函数引用了外层函数的变量
    - 外层函数返回内层函数

11. 迭代器
    迭代器是实现了迭代器协议的对象，用于惰性地逐个生成数据序列，并在遍历结束后自动停止。
    - `__iter__()`：返回迭代器对象自身。
    - `__next__()`：返回序列中的下一个元素；若再无元素，则抛出 StopIteration 异常。
    与可迭代对象（Iterable）的区别：
    可迭代对象（如 list、tuple、dict）实现了 __iter__()，可返回一个迭代器，但自身并非迭代器。

12. 生成器
    生成器是使用 yield 语句定义的特殊函数，它自动实现迭代器协议，用于惰性生成序列。
    - 生成器函数 每次调用 next() 方法时，函数会暂停执行，返回 yield 后面的表达式值。
    - 生成器表达式 类似列表推导式，但用圆括号

13. 并发、并行、同步、异步
    并行并发 描述的是系统整体（或 CPU 层面）的宏观行为表现。
    同步异步 描述的是单个函数调用（或代码层面）的微观交互机制。
    并发：在一段时间内，当CPU面对多个任务时，会将每个任务交替着执行一段时间。
    并行：同一时刻，每个核心独立执行不同任务
    同步：发起任务后必须等待该任务完成才能执行后续任务 当前执行流被阻塞
    异步：发起任务后不必等待即可继续执行其他任务

    同步 + 并发	多线程/多进程阻塞 I/O	    多个线程各自同步等待数据，OS 调度线程轮换。
    同步 + 并行	多进程 CPU 密集型计算	    多个核心同时执行独立的同步计算任务。
    异步 + 并发	单线程事件循环（asyncio）	一个线程内交替处理多个非阻塞 I/O 请求（高并发低开销）。
    异步 + 并行	多进程 + 事件循环	        每个进程内跑异步事件循环，兼顾多核与高 I/O 并发。

14. 协程
    一种可以被挂起，挂起后可以被恢复的函数
    原因：CPU在多个线程之前切换是有成本的
    - 协程函数 定义时使用async def关键字
    - 协程对象 调用协程函数时返回一个协程对象
    - await
      - 挂起 暂停当前协程执行
      - 等待 安排await后对象(协程对象、Future对象、任务对象)执行 等待其完成
        - 对象有IO操作，事件循环会切换到其他任务执行
        - 对象没有IO操作，不会发生任务切换
      - 恢复 拿到await后对象的结果 恢复之前挂起的协程执行 
多任务同步执行
```python
import asyncio
import time


async def work(n, delay):
    print(f"work {n} start")
    print(f"work {n} working")
    await asyncio.sleep(delay)
    print(f"work {n} done")
    return f"work {n} result"


async def main():
    start_time = time.time()

    coroutine1 = work(1, 2)
    coroutine2 = work(2, 2)
    coroutine3 = work(3, 2)

    result1 = await coroutine1
    print(result1)
    result2 = await coroutine2
    print(result2)
    result3 = await coroutine3
    print(result3)

    end_time = time.time()
    print(f"total time: {end_time - start_time}")


asyncio.run(main())
```

多任务异步执行
```python
import asyncio
import time


async def work(n, delay):
    print(f"work {n} start")
    print(f"work {n} working")
    await asyncio.sleep(delay)
    print(f"work {n} done")
    return f"work {n} result"


async def main():
    start_time = time.time()
    # 注册到事件循环里
    # task1 = asyncio.create_task(work(1, 2))
    # task2 = asyncio.create_task(work(2, 2))
    # task3 = asyncio.create_task(work(3, 2))
    # 把多个协程对象丢给事件循环
    results = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print(results)

    # result1 = await task1
    # print(result1)
    # result2 = await task2
    # print(result2)
    # result3 = await task3
    # print(result3)

    end_time = time.time()
    print(f"total time: {end_time - start_time}")


asyncio.run(main())
```
