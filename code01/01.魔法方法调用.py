"""
class Foo

print(Foo().think.different.itcast)
要求输出结果是 think different itcast

"""


class Foo(object):
    def __init__(self):
        self.pwd = 10

    # 魔法方法表示的是如果从类字典和对象字典无法找到的参数，最后会在这里查找
    def __getattr__(self, item):
        print(item, end=" ")
        return self

    # 这个魔法方法是主线，通过这个方法来执行的先调用类字典和对象字典查找变量 也就是点之后的操作。然后再去__getattr__取查找变量
    # 一般这个方法不会去直接改动，容易使程序栈溢出，导致死循环
    def __getattribute__(self, item):
        return self.pwd

    def __str__(self):
        return ""


# print(Foo().think.different.itcast)
print(Foo().think)