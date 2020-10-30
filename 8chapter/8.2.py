# coding=utf-8

'''

使用类进行解耦   额外添加一个类，使程序进行解耦（简单工厂模式）

设计模式
解决某一类问题使用的模板

'''


class CellCar(object):
    def __init__(self):
        self.factory = Factory()  # 定义工厂类的对象

    def book(self, type_name):
        return self.factory.select_car_type(type_name)

class Factory(object):
    def select_car_type(self, car_type):
        if car_type == "Toyata":
            return Toyata()
        elif car_type == "Honda":
            return Honda()
        elif car_type == "Benz":
            return Benz()

class Car(object):

    def Move(self):
        print("车在移动...")

    def Run(self):
        print("车在跑...")

    def Stop(self):
        print("车停下来了...")


class Toyata(Car):
    pass

class Honda(Car):
    pass

class Benz(Car):
    pass


cellcar = CellCar()
car = cellcar.book("Toyata")

car.Run()
car.Move()
car.Stop()