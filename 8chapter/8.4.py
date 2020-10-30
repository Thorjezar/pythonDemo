# coding=utf-8

'''

单例模式

举个常见的单例模式例子，我们日常使用的电脑上都有一个回收站，在整个操作系统中，回收站只能有一个实例，
整个系统都使用这个唯一的实例，而且回收站自行提供自己的实例。因此回收站是单例模式的应用。

确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。
考虑__new__(cls)方法

只执行一次的init()方法

'''

class Singleton(object):
    __instance = None
    __init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
        # if not cls.__instance:
        #     cls.__instance = object.__new__(cls)
        #     return cls.__instance

    @classmethod
    def get_instance(cls):
        return cls.__instance

    @classmethod
    def get_init_flag(cls):
        return cls.__init_flag

    @classmethod
    def set_init_flag(cls):
        cls.__init_flag = True

    def __init__(self, name):
        # if self.get_init_flag == False:
        #     self.name = name
        #     self.set_init_flag
        if Singleton.__init_flag == False:
            self.name = name
            Singleton.__init_flag = True

a = Singleton("啊啊")
print(id(a))
print(a.name)
b = Singleton("啵啵")
print(id(b))
print(b.name)