# coding=utf-8

'''

__new__方法
程序创建的时候调用的

python中的构造方法包含两个方法
__init__()只负责初始化
__new__()只负责创造对象

总结
__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，
或者直接是object的__new__出来的实例
__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节

'''
class A(object):
    def __init__(self):
        print("=" * 8 + "init" + "=" * 8)

    def __str__(self):
        print("=" * 8 + "str" + "=" * 8)
        return "打印对象描述"

    def __del__(self):
        print("=" * 8 + "del" + "=" * 8)

    def __new__(cls):  # cls 此时指向的是A所指的类对象
        # print(id(cls))
        print("=" * 8 + "new" + "=" * 8)
        return object.__new__(cls)   # 真正的创建对象的方法

# print(id(A))

a = A()
