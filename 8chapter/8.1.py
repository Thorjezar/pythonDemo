# coding=utf-8

'''

耦合性
修改一处代码，及将引起另一处代码的修改

解耦合：使用函数 去解除类之间的方法 的耦合

'''

class CellCar(object):
    def book(self, type_name):
        return select_car_type(type_name)

def select_car_type(car_type):      # 这边解耦
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
