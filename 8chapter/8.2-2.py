# coding=utf-8

'''

工厂方法模式

在父类中定义的方法不去实现具体操作，
在继承的子类中去重写方法来实现

最后来看看工厂方法模式的定义
定义了一个创建对象的接口(可以理解为函数)，但由子类决定要实例化的类是哪一个，工厂方法模式让类的实例化推迟到子类，
抽象的CarStore提供了一个创建对象的方法createCar，也叫作工厂方法。

子类真正实现这个createCar方法创建出具体产品。 创建者类不需要直到实际创建的产品是哪一个，
选择了使用了哪个子类，自然也就决定了实际创建的产品是什么。

'''

class Store(object):

    # 在父类中定义的方法，不去实现具体操作
    def select_car(self):
        pass

    def Book(self, car_name):
        return self.select_car(car_name)

class BWMStore(Store):

    # 在子类中重写父类方法，去实现具体操作
    def select_car(self, car_name):
        pass

class AudiStore(Store):

    def Book(self, car_name):
        pass
bwm_store = BWMStore()
bwm = bwm_store.Book("7系")

