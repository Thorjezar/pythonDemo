# coding=utf-8

'''
多态
多态就要绑定继承来看，多态的含义是 定义的时候不知道具体的调用
程序运行的时候传入的参数不同，反应出来不同
python既支持面向过程，又支持面向对象
面向过程的四个特性
抽象、封装、继承、多态

'''
class Demo(object):
    def show(self):
        print("这里是Demo下的方法")

class RealOne(Demo):
    def show(self):
        print("这里是RealOne的方法")

class RealTwo(Demo):
    def show(self):
        print("这里是RealTwo的方法")

class RealThree(RealOne, RealTwo):
    def show(self):
        print("这里是RealThree的方法")
        super().show()

def Tell(demo):    # python是弱类型语言，动态的去调用。等到运行的时候才去调用
    demo.show()

demo = Demo()
r1 = RealOne()
r2 = RealTwo()
r3 = RealThree()

Tell(r3)


