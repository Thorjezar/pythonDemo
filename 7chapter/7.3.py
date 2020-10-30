# coding=utf-8

'''
创建对象后，python解释器默认调用__init__()方法；
当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法

总结
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不为1，
比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，
如果再调用1次del，此时会真的把对象进行删除

import sys
sys.getrefcount(变量) 这个方法的作用是，算出变量 引用的对象 的类，有多少个引用计数
结果会比实际的数量加1
因为在sys调用这个方法的时候，会在内部生成一个对象指向变量
所以会比实际的多一个
'''
class Demo:

    def __init__(self, new_name):
        self.name = new_name
    # del方法，在引用变量等于0时会自动调用
    def __del__(self):
        print(self.name + "对象被干掉了")

demo1 = Demo("demo1")
demo2 = Demo("demo2")
demo3 = demo1  # 引用计数+1

del demo1
print("=" * 8)
del demo2
print("=" * 8)
del demo3
print("=" * 8)

