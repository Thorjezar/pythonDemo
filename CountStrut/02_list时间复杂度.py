"""

list的各种功能的时间复杂度
timeit模块
timeit模块可以用来测试一小段Python代码的执行速度。

class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
Timer是测量小段代码执行速度的类。

stmt参数是要测试的代码语句（statment）；

setup参数是运行代码时需要的设置；

timer参数是一个定时器函数，与平台有关。

timeit.Timer.timeit(number=1000000)
Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。
方法返回执行代码的平均耗时，一个float类型的秒数。

"""
from timeit import Timer


def demo1():
    l = []
    for i in range(1000):
        l = l + [i]


def demo2():
    l = []
    for i in range(1000):
        l.append(i)


def demo3():
    l = [i for i in range(1000)]


def demo4():
    l = list(range(1000))


t1 = Timer("demo1()", "from __main__ import demo1")
print("concat ", t1.timeit(number=1000), "seconds")
t2 = Timer("demo2()", "from __main__ import demo2")
print("append ", t2.timeit(number=1000), "seconds")
t3 = Timer("demo3()", "from __main__ import demo3")
print("comprehension ", t3.timeit(number=1000), "seconds")
t4 = Timer("demo4()", "from __main__ import demo4")
print("list range ", t4.timeit(number=1000), "seconds")

