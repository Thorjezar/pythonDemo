# coding=utf-8

'''
测试__all__
如果一个文件中有__all__变量，那么也就意味着这个变量中的元素，不会被from xxx import *时导入
'''
__all__ = ["Demo", "demo1"]
class Demo(object):
    def __init__(self):
        pass

    def demo1(self):
        print("类中的方法demo1")

def demo1():
    print("函数demo1")

def demo2():
    print("函数demo2")
